class car:
    color=""
    speed=0
    def upspeed(self,value):
        self.speed += value

    def downspeed(self,value):
        self.speed -= value
mycar1=car()
mycar1.color="빨강"; mycar1.speed=0
mycar2=car()
mycar2.color="파랑"; mycar2.speed=0
mycar3=car()
mycar3.color="노랑"; mycar3.speed=0
mycar1.upspeed(30)
print("자동차1의 색상 %s 현재속도는 %dkm입니다."%(mycar1.color,mycar1.speed))
mycar2.upspeed(30)
print("자동차2의 색상 %s 현재속도는 %dkm입니다."%(mycar2.color,mycar2.speed))
mycar3.downspeed(10)
print("자동차3의 색상 %s 현재속도는 %dkm입니다."%(mycar3.color,mycar3.speed))





