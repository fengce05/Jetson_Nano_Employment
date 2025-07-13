import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam=cv2.VideoCapture(camSet)
pyLogo=cv2.imread('py.jpg')
pyLogo=cv2.resize(pyLogo,(75,75))
pyLogoGray=cv2.cvtColor(pyLogo,cv2.COLOR_BGR2GRAY)
cv2.imshow('py Logo Gray',pyLogoGray)
cv2.moveWindow('py Logo Gray',800,0)
_,BGMask = cv2.threshold(pyLogoGray,254,255,cv2.THRESH_BINARY)
cv2.imshow('BG Mask',BGMask)
cv2.moveWindow('BG Mask',900,0)
FGMask=cv2.bitwise_not(BGMask)
cv2.imshow('FGMask',FGMask)
cv2.moveWindow('FGMask',1000,0)
FG=cv2.bitwise_and(pyLogo,pyLogo,mask=FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG',1100,0)

BW=75
BH=75
Xpos=10
Ypos=10
dx=1
dy=1

while True:
    ret, frame=cam.read()
    ROI=frame[Ypos:Ypos+BH,Xpos:Xpos+BW]
    ROIBG=cv2.bitwise_and(ROI,ROI,mask=BGMask) 
    cv2.imshow('ROIBG', ROIBG)
    cv2.moveWindow('ROIBG',1200,0)

    ROInew=cv2.add(FG,ROIBG)
    cv2.imshow('ROInew',ROInew)
    cv2.moveWindow('ROInew',1300,0)

    frame[Ypos:Ypos+BH,Xpos:Xpos+BW] = ROInew

    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCam',0,0)
    Xpos=Xpos+dx
    Ypos=Ypos+dy
    if Xpos <=0 or Xpos+BW>=dispW:
        dx=dx*(-1)
    if Ypos<= 0 or Ypos+BH>=dispH:
        dy=dy*(-1)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()