def where(a,b,c,d):#a=
    a=int(input("어디로 옮기겠습니까?"))
    if a==b :
        print("같은 기둥입니다")
    else :
        for i in range(1,8):
            if d[b-1][i-1]==0:
                continue
            elif d[b-1][i]<d[b-1][i-1]:
                c=d[b-1][i]
        print("%d번째 기둥에서 %d번재 기둥으로 %d인 탑을 옮겼습니다"%(b,a,c))
