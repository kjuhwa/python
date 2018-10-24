import datetime

dt= datetime.date(2018,1,3)
print( dt )
print( dt.year, dt.month, dt.day)
tm = datetime.time(11,10,12)
print( tm )
print( tm.hour, tm.minute,tm.second)
dttm = datetime.datetime(1999,2,3,4,10,30)
print( dttm)
sysdate = datetime.datetime.now()
print(sysdate)
print( sysdate.year, sysdate.month, sysdate.day,
       sysdate.hour,sysdate.minute,sysdate.second)
