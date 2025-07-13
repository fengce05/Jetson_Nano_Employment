import jetson_inference
import jetson_utils
import cv2
import time
import numpy as np

timeStamp=time.time()
fpsFilt=0
net=jetson_inference.detectNet('ssd-mobilenet-v2',threshold=.5)
dispW=640
dispH=480
flip=2
font=cv2.FONT_HERSHEY_SIMPLEX
camSet='nvarguscamerasrc wbmod=3 tnr-mode=2 tnr-strength=1 ee-mode=2 ee-strength=1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance  contrast=1.3 brightness=-.1 saturation=1.2 ! appsink drop=true'
cam1=cv2.VideoCapture(camSet)

# cam1=cv2.VideoCapture('/dev/video1')
# cam1.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
# cam1.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

# cam=jetson_utils.gstCamera(dispW,dispH,'0')
# cam=jetson_utils.gstCamera(dispW,dispH,'/dev/video1')
# display=jetson_utils.glDisplay()
# while display.IsOpen():
while True:
    # img,width,height=cam.CaptureRGBA()
    _,img=cam1.read()
    height=img.shape[0]
    width=img.shape[1]
    frame=cv2.cvtColor(img,cv2.COLOR_BGR2RGBA).astype(np.float32)
    frame=jetson_utils.cudaFromNumpy(frame)
    detections=net.Detect(frame,width,height)
    for detect in detections:
        #print(detect)
        ID=detect.ClassID
        top=int(detect.Top)
        left=int(detect.Left)
        bottom=int(detect.Bottom)
        right=int(detect.Right)
        item=net.GetClassDesc(ID)
        print(item,top,left,bottom,ID)
        tk=1
        if item == 'cat':
            tk=-1
        cv2.rectangle(img,(left,top),(right,bottom),(0,255,0),tk)
        cv2.putText(img,item,(left,top+20),font,.75,(0,0,255),2)
        print(item)
    # print(detections)
    # display.RenderOnce(img,width,height)
    dt=time.time()-timeStamp
    timeStamp=time.time()
    fps=1/dt
    fpsFilt=.9*fpsFilt+.1*fps
    # print(str(round(fps,1))+' fps ')
    cv2.putText(img,str(round(fpsFilt,1))+' fps',(0,30),font,1,(0,0,255),2)
    cv2.imshow('detCam',img)
    cv2.moveWindow('detCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam1.release()
cv2.destroyAllWindows()
