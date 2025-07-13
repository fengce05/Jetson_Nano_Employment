import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi,50)
y=np.sin(x)
y2=np.cos(x-np.pi/2)
# y3=np.square(x)+4
plt.grid(True)
plt.xlabel('My X Values')
plt.ylabel('My Y Values')
plt.title('My First Graph')
#plt.axis([0,5,2,11])
plt.plot(x,y,'b^',linewidth=3,markersize=7,label='Sin(x)')
plt.plot(x,y2,'r-',linewidth=3,markersize=7,label='Cos(x)')
# plt.plot(x,y3,'g-^',linewidth=3,markersize=7,label='Green Line')
plt.legend(loc='upper center')
plt.show()
