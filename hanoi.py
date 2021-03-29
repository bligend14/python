import toplace
import toplace2
top=[0,0,0]
hanoi=[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
print('',"-"*20,"\n","하노이 탑 게임\n","-"*20)
a=toplace.where()
top[a-1]=1
hanoi[a-1]=[8,7,6,5,4,3,2,1]
print("하노이 탑은 %d번째 기둥에 있습니다"%a)
while 1 :
    choice1=0
    choice=int(input("기둥을 선택하시오:"))
    choice1=toplace.measure(top,choice,hanoi,choice1)
    if choice1==0:
        continue
    choice2=input("옮기겠습니까?")
    if choice2=='no':
        continue
    elif choice2=='yes':
        toplace2.where(choice1.choice)

