class Rectangle:
    def __init__(self,c,w,l):
        self.width=w
        self.length=l
        self.color=c
    def area(self):
        self.area=self.width*self.length
        return self.area
    def per(self):
        self.perimeter=2*self.width+2*self.length
        return self.perimeter

c1='red'
w1=3
l1=4
rect1=Rectangle(c1,w1,l1)
areaRect1=rect1.area()
print(areaRect1)

c2='red'
w2=7
l2=3.2
rect2=Rectangle(c2,w2,l2)
areaRect2=rect2.area()
print(areaRect2)

print('Rectangle 1 is:',rect1.color)
print('Rectangle 2 is:',rect2.color)

per1 = rect1.per()
print('The',rect1.color,'Rectangle has Perimeter', per1)
