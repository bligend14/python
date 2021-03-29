from datetime import datetime
today = datetime.now()#오늘
print("년: %s"%(today.year))
print("월: %s"%(today.month))
print("일: %s"%(today.day))
print(today.strftime("%Y/%m/%d %H:%M:%S"))
