import cv2
print(cv2.__version__)
def nothing(x):
    pass
cv2.namedWindow('Blended')
cv2.createTrackbar('BlendValue','Blended',50,100,nothing)

dispW=320
dispH=240
flip=2

cvLogo=cv2.imread('cv.jpg')
cvLogo=cv2.resize(cvLogo,(320,240))
cvLogoGray=cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY)
cv2.imshow('cv Logo Gray',cvLogoGray)
cv2.moveWindow('cv Logo Gray',0,350)

_,BGMask=cv2.threshold(cvLogoGray,225,255,cv2.THRESH_BINARY)
cv2.imshow('BG Mask',BGMask)
cv2.moveWindow('BG Mask',385,100)

FGMask=cv2.bitwise_not(BGMask)
cv2.imshow('FG Mask',FGMask)
cv2.moveWindow('FG Mask',385,350)

FG=cv2.bitwise_and(cvLogo,cvLogo,mask=FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG',703,350)

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
# cam=cv2.VideoCapture(1)
while True:
    ret, frame=cam.read()
    BG=cv2.bitwise_and(frame,frame,mask=BGMask) 
    cv2.imshow('BG', BG)
    cv2.moveWindow('BG',703,100)

    compImage=cv2.add(BG,FG)
    cv2.imshow('compImage', compImage)
    cv2.moveWindow('compImage',1017,100)

    BV1=cv2.getTrackbarPos('BlendValue','Blended')/100
    BV2=1-BV1

    Blended =cv2.addWeighted(frame,BV1,cvLogo,BV2,0)
    cv2.imshow('Blended',Blended)
    cv2.moveWindow('Blended',1017,350)

    FG2=cv2.bitwise_and(Blended,Blended,mask=FGMask)
    cv2.imshow('FG2',FG2)
    cv2.moveWindow('FG2',1324,100)  

    compFinal=cv2.add(FG2,BG)
    cv2.imshow('compFinal',compFinal)
    cv2.moveWindow('compFinal',1324,350)  

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,100)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()