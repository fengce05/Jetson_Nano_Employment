from threading import Thread
import cv2
import time
import numpy as np
font=cv2.FONT_HERSHEY_SIMPLEX
startTime=time.time()
class vStream:
    def __init__(self,src,width,height):
        self.width=width
        self.height=height
        self.capture=cv2.VideoCapture(src)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
        self.thread=Thread(target=self.update,args=())
        self.thread.daemon=True
        self.thread.start()
    def update(self):
        while True:
            _,self.frame = self.capture.read()
            self.frame2=cv2.resize(self.frame,(self.width,self.height))
    def getFrame(self):
        return self.frame2

dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam1=vStream(1,dispW,dispH)
cam2=vStream(camSet,dispW,dispH)
dtav=0
while True:
    try:
        myFrame1=cam1.getFrame()
        myFrame2=cam2.getFrame()
        myFrame3=np.hstack((myFrame1,myFrame2))
        dt=time.time()-startTime
        startTime=time.time()
        dtav=0.9*dtav+.1*dt
        fps=1/dtav
        cv2.rectangle(myFrame3,(0,0),(100,40),(0,0,255),-1)
        cv2.putText(myFrame3,str(round(fps,1))+' FPS',(0,25),font,.75,(0,255,255),2)
        cv2.imshow('ComboCam',myFrame3)
        cv2.moveWindow('ComboCam',0,0)
    except:
        print('frame not available')
    if cv2.waitKey(1)==ord('q'):
        cam1.capture.release()
        cam2.capture.release()
        cv2.destroyAllWindows()
        exit(1)
        break