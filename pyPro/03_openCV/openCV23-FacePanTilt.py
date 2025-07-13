import cv2
print(cv2.__version__)
import numpy as np
from adafruit_servokit import ServoKit
kit=ServoKit(channels=16)

pan=90
tilt=90
kit.servo[0].angle=pan
kit.servo[1].angle=tilt

dispW=640
dispH=480
flip=2

cam=cv2.VideoCapture(1)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
face_cascade=cv2.CascadeClassifier('/home/fc/Desktop/pyPro/cascade/face.xml')
eye_cascade=cv2.CascadeClassifier('/home/fc/Desktop/pyPro/cascade/eye.xml')
while True:   
    ret, frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,135),2)
        Xcent=x+(w/2)
        Ycent=y+(h/2)
        errorPan = Xcent-(dispW/2)
        errorTilt = Ycent-(dispH/2)
        if abs(errorPan>10):
            pan=pan-errorPan/50
        if abs(errorTilt)>10:
            tilt=tilt-errorTilt/50
        if pan>180:
            pan=180
            print("Pan Out of  Range")   
        if pan<0:
            pan=0
            print("Pan Out of  Range") 
        if tilt>180:
            tilt=180
            print("Tilt Out of  Range") 
        if tilt<0:
            tilt=0
            print("Tilt Out of  Range") 
        kit.servo[0].angle=pan
        kit.servo[1].angle=tilt
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame [y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
        break
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()