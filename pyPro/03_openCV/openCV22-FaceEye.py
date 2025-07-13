import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# cam=cv2.VideoCapture(camSet)
cam=cv2.VideoCapture(1)
# cam.set(cv2.CAP_PROP_FPS, 30)
face_cascade=cv2.CascadeClassifier('/home/fc/Desktop/pyPro/cascade/face.xml')
eye_cascade=cv2.CascadeClassifier('/home/fc/Desktop/pyPro/cascade/eye.xml')
while True:
    ret, frame=cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray=gray[y:y+h,x:x+w]
        Roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.3,5)
        for (xEye,yEye,wEye,hEye) in eyes:
            cv2.circle(Roi_color,(int(xEye+wEye/2),int(yEye+hEye/2)),6,(255,0,0),-1)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
