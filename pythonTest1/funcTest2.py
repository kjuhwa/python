
def hap(a,b):
    return a+b

def gop(a,b):
    return a*b

def circle_area(r):
    return r**2*3.14

def 원기둥부피(r,h):
    return r**2*h*3.14

def 원뿔부피(r,h):
    return 1/3*r**2*h*3.14

def 윤년(년도):
    return '윤년' if 년도%4==0 and 년도%100 !=0 or 년도%400==0 else '윤년아님'

def 절대값(x,y):
    return abs(x) + abs(y)

def 합(x):
    sum = 0
    for n in range(x+1):
        sum+=n
    return sum


rst = hap(10,20)
print(rst)

rst = gop(10,20)
print(rst)

rst = circle_area(5)
print(rst)

rst = 원기둥부피(5,10)
print(rst)

rst = 원뿔부피(5,10)
print(rst)

rst = 윤년(2020)
print(rst)

rst = 절대값(-2020, 1)
print(rst)

rst = 합(100)
print(rst)
