import math

class circle:
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        area=math.pi*self.radius**2
        return area
    def getlen(self):
        len1=2*3.141592*self.radius
        return len1
a=int(input("반지름을 입력하세요: "))        
cir = circle(a)
cir.__init__(a)
print("반지름: %d"%(cir.radius))
print("넓이: %.2f \n"%(float(cir.getArea())))
print("둘레: %.2f \n"%(float(cir.getlen())))
