import jetson_inference
import jetson_utils

net=jetson_inference.detectNet('ssd-mobilenet-v2',threshold=.5)
cam=jetson_utils.gstCamera(640,480,'/dev/video0')