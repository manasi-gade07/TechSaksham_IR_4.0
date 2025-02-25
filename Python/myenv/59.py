from datetime import datetime,date,time,timedelta
now = datetime.now()
print(now)
d= date.today()
print(now.strftime('%B/%Y,%d,%H:%M')) #24 hrs
print(now.strftime('%B/%Y,%d,%I:%M')) # 12 hrs
a = timedelta(days=10)
b =timedelta (now.day)
print(a+b)

