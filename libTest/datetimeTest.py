import datetime

dt = datetime.date(2018,1,3)
print(dt)
print(dt.year, dt.month, dt.day)
tm = datetime.time(11,10,12)
print(tm)
print(tm.hour, tm.minute, tm.second)
dttm = datetime.datetime(2018,1,3,10,11,12)
print(dttm)
sysdate = datetime.datetime.now()
print(sysdate)
