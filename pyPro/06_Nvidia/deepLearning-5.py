import jetson_inference
import jetson_utils
import cv2
import time

timeStamp=time.time()
fpsFilt=0

net=jetson_inference.detectNet('ssd-mobilenet-v2',threshold=.5)
dispW=1280
dispH=720
# cam=jetson_utils.gstCamera(dispW,dispH,'0')
cam=jetson_utils.gstCamera(dispW,dispH,'/dev/video1')
display=jetson_utils.glDisplay()
while display.IsOpen():
    img,width,height=cam.CaptureRGBA()
    detections=net.Detect(img,width,height)
    display.RenderOnce(img,width,height)
    dt=time.time()-timeStamp
    timeStamp=time.time()
    fps=1/dt
    fpsFilt=.9*fpsFilt+.1*fps
    print(str(round(fps,1))+' fps ')


