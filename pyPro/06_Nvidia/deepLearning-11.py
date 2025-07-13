import threading
import jetson_inference
import jetson_utils
import numpy as np
import time
import pyttsx3


speak=True
item='welcome to My Identify Are you Ready to Rumble?'
confidence=0
itemOld=''


import cv2
print(cv2.__version__)
width=1280
height=720
flip=2

engine=pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('voice','english+f2')

def sayItem():
    global speak
    global item
    while True:
        if speak == True:
            text=item
            engine=pyttsx3.init()
            engine.setProperty('rate',150)
            engine.setProperty('voice','english+f2')
            engine.say(text)
            engine.runAndWait()
            speak=False
x=threading.Thread(target=sayItem,daemon=True)
x.start()
cam=cv2.VideoCapture('/dev/video1')
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
net=jetson_inference.imageNet('googlenet')
font=cv2.FONT_HERSHEY_SIMPLEX
timeMark=time.time()
fpsFilter=0
while True:
    ret,frame = cam.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    img=jetson_utils.cudaFromNumpy(img)
    if speak==False:
        classID,confidence=net.Classify(img,width,height)
        if confidence>=.3:
            item=net.GetClassDesc(classID)
            if item!=itemOld:
                speak=True
        if confidence<.3:
            item=''
        itemOld=item
    dt=time.time()-timeMark
    timeMark=time.time()
    fps=1/dt
    fpsFilter=.95*fpsFilter+.05*fps
    cv2.putText(frame,str(round(fpsFilter,1))+' fps '+item+' '+str(round(confidence,2)),(0,30),font,1,(0,0,255),2)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(10) == ord('q'):
        break  # Increase waitKey delay to ensure proper key detection
cam.release()
cv2.destroyAllWindows()
