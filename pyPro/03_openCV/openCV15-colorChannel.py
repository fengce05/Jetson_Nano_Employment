import cv2
import numpy as np
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
# cam=cv2.VideoCapture(1)
blank=np.zeros([480,640,1],np.uint8)
while True:
    ret, frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    b,g,r=cv2.split(frame)
    
    blue=cv2.merge((b,blank,blank))
    green=cv2.merge((blank,g,blank))
    red=cv2.merge((blank,blank,r))
    g[:]=g[:]*.15
    merge=cv2.merge((b,g,r))

    # print(frame[50,45,0])
    # b=cv2.split(frame)[0]
    # g=cv2.split(frame)[1]
    # r=cv2.split(frame)[2]
    cv2.imshow('blue',blue)
    cv2.moveWindow('blue',700,0)
    cv2.imshow('green',green)
    cv2.moveWindow('green',0,500)
    cv2.imshow('red',red)
    cv2.moveWindow('red',700,500)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    # cv2.imshow('blank',blank)
    # cv2.moveWindow('blank',1350,0)
    cv2.imshow('merge',merge)
    cv2.moveWindow('merge',1350,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
