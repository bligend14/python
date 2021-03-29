class calculator:
    def set(self,x,y):
        self.fir=x
        self.sec=y
    def add(self):
        result=self.fir  + self.sec
        return result
hap1=calculator()
a=int(input("첫번째값을 입력하세요"))
b=int(input("두번째값을 입력하세요"))
hap1.set(a,b)
print("%d + %d = %d"%(hap1.fir,hap1.sec,hap1.add()))
