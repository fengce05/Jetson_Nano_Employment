import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
BW=int(.2*dispW)
BH=int(.2*dispH)
posX=10
posY=270
dx=2
dy=2

# cam=cv2.VideoCapture(1)
while True:
    ret, frame=cam.read()
    roi = frame[posY:posY+BH,posX:posX+BW].copy()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[posY:posY+BH,posX:posX+BW] = roi
    cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(255,0,0),3)
    cv2.imshow('nanoCam',frame)
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
