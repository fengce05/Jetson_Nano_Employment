import jetson_inference
import jetson_utils

cam=jetson_utils.gstCamera(640,480,'/dev/video0')
disp=jetson_utils.glDisplay()
font=jetson_utils.cudaFont()
net=jetson_inference.imageNet('googlenet')

while disp.IsOpen():
    frame,width,height=cam.CaptureRGBA()
    classID,confident=net.Classify(frame,width,height)
    item=net.GetClassDesc(classID)
    font.OverlayText(frame,width,height,item,5,5,font.Magenta,font.Blue)
    disp.RenderOnce(frame,width,height)
