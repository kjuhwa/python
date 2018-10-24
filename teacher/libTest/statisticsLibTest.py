#전역변수
#클래스
#일반함수
from statistics import mean,median,stdev
my=[10,20,30,40]
print( dir(__builtins__) ) #별도import 없이 사용
print( sum( my ) )
print( max( 10,20,30,40 ) )
print( max( my ))
print( min(my))
print( mean(my))
print( median(my))
print( stdev(my))
