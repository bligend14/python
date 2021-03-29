from datetime import datetime
today=datetime.now()
print(today.strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))
print("#1년 더하기")
out = today.replace(year=(today.year)+1)
print(out.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년"))


