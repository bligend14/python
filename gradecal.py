class Grade:
    title="- 3과목 합계 평균 "
    def __init__(self,name,kor,eng,math):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
    def getsum(self):
        self.sum1=self.kor+self.eng+self.math
        return self.sum1
    def getavg(self):
        avg=self.sum1/3
        return avg
n1=input("이름:")
k1=int(input("국어: "))
e1=int(input("영어: "))
m1=int(input("수학: "))
s1= Grade(n1,k1,e1,m1)
print(s1.title)
print("%s 님의 3과목 합계:%d, 평균: %.1f입니다"%(s1.name,s1.getsum(),s1.getavg()))