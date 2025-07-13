from threading import Thread
import time
def BigBox(color,l):
    while True:
        print(color,'Big Box is Open of length',l)
        time.sleep(5)
        print(color,'Big Box is Closed of length',l)
        time.sleep(5)
def smallBox(color,l):
    while True:
        print(color,'Small Box is Open of length',l)
        time.sleep(1)
        print(color,'Small Box is Closed of length',l)
        time.sleep(1)
c='red'
x=5
bigBoxThread=Thread(target=BigBox,args=(c,x))
c='blue'
x=4
smallBoxThread=Thread(target=smallBox,args=(c,x))
bigBoxThread.daemon=True
smallBoxThread.daemon=True
bigBoxThread.start()
smallBoxThread.start()
while True:
    pass