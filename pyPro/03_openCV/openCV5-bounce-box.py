import cv2
import torch

print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
dispW=int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
dispH=int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
BW=int(.25*dispW)
BH=int(.15*dispH)
posX=10
posY=270
dx=2
dy=2

# cam=cv2.VideoCapture(1)
while True:
    ret, frame=cam.read()
    cv2.moveWindow('nanoCam',0,0)
    frame=cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(255,0,0),-1)
    cv2.imshow('piCam',frame)
    posX=posX+dx
    posY=posY+dy
    if posX <=0 or posX+BW>=dispW:
        dx=dx*(-1)
    if posY<= 0 or posY+BH>=dispH:
        dy=dy*(-1)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
