def wonwin(a,b):
    if a=='가위':
        if b=='가위':
            print("무승부입니다")
        elif b=='바위':
            print("컴퓨터의 승리입니다")
        elif b=='보':
            print("나의 승리입니다")
    elif a=='바위':
        if b=='가위':
            print("나의 승리입니다")
        elif b=='바위':
            print("무승부입니다")
        elif b=='보':
            print("컴퓨터의 승리입니다")
    elif a=='보':
        if b=='가위':
            print("컴퓨터의 승리입니다")
        elif b=='바위':
            print("나의 승리입니다")
        elif b=='보':
            print("무승부입니다")
def intro():
    print('-'*20)
    print("가위 바위 보 게임")
    print('-'*20)