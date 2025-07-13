# libcamera-vid --timeout=0 --width 1640 --height 1232 --framerate=30 --bitrate=2000000 --awb auto --nopreview -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=0.0.0.0 port=8554

import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet=' tcpclientsrc host=192.168.3.17 port=8554 ! gdpdepay ! rtph264depay ! h264parse ! nvv4l2decoder  ! nvvidconv flip-method='+str(flip)+' ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+',format=BGR ! appsink  drop=true sync=false '

cam=cv2.VideoCapture(camSet)

while True:
    ret,frame = cam.read()
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


