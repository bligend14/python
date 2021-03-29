def where():
    import random
    a=random.randint(1,3)
    return a;
def measure(a,b,d,e):
    if a[b-1]== 1:
        for i in range(1,8):
            if d[b-1][i-1]==0:
                continue
            elif d[b-1][i]<d[b-1][i-1]:
                c=d[b-1][i]
        print("%d번째 기둥에는 %s중에 움직일 수 있는건 %s가 있습니다"%(b,list(d[b-1]),c))
    elif a[b-1]== 0:
        print("%d번째 기둥에는 %s중에 움직일 수 있는건 없습니다"%(b,list(d[b-1])))
        e=0;
        return e; 