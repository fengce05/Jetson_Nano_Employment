import jetson_inference
import jetson_utils
import cv2
import numpy as np
import time
width = 640
height = 480
dispW = width
dispH = height
flip=2
# cam=jetson_utils.gstCamera(width,height,'/dev/video0')
# cam=jetson_utils.gstCamera(width,height,'0')

# display=jetson_utils.glDisplay()
# font=jetson_utils.cudaFont()
# camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam1=cv2.VideoCapture(camSet)
cam1=cv2.VideoCapture('/dev/video1')
cam1.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam1.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
net=jetson_inference.imageNet('googlenet',['--model=/home/fc/Downloads/jetson-inference/python/training/classification/myModel/resnet18.onnx',
                                           '--input_blob=input_0',
                                           '--output_blob=output_0',
                                           '--labels=/home/fc/Downloads/jetson-inference/myTrain/labels.txt'])
font=cv2.FONT_HERSHEY_SIMPLEX
timeMark=time.time()
fpsFilter=0


while True:
    # frame,width,height=cam.CaptureRGBA(zeroCopy=1)
    _,frame=cam1.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA).astype(np.float32)
    img=jetson_utils.cudaFromNumpy(img)
    classID,confidence=net.Classify(img,width,height)
    item=''
    item =net.GetClassDesc(classID)
    dt=time.time()-timeMark
    fps=1/dt
    fpsFilter=.95*fpsFilter+.05*fps
    timeMark=time.time()
    # font.OverlayText(frame,width,height,str(round(fpsFilter,1))+' fps '+item,5,5,font.Magenta,font.Blue)
    # display.RenderOnce(frame,width,height)
    # frame=jetson_utils.cudaToNumpy(frame,width,height,4)
    # frame=cv2.cvtColor(frame,cv2.COLOR_RGBA2BGR).astype(np.uint8)
    cv2.putText(frame,str(round(fpsFilter,1))+' fps '+item,(0,30),font,1,(0,0,255),2)
    cv2.imshow('recCam',frame)
    cv2.moveWindow('recCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam1.release()
cv2.destroyAllWindows()