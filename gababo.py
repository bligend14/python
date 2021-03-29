import whowin; import choice
from continew import *;

whowin.intro()
me,computer,ans='','','y'
while ans == 'y':
	computer=choice.decide(computer)
	me=input("나:")
	print("컴퓨터: %s"%computer)
	whowin.wonwin(me,computer)
	ans=question(ans)

