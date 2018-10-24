def hap(a,b):
    return a+b

def gop(a,b): #인자,인수,아규먼트
    return a*b

def circle_area(r):
    return r**2*3.14

def mToMile( m ):
    return m*0.000621

def cylinderVolume(r,h):
    return r**2*3.14*h

def coneVolume(r,h):
    return r**2*3.14*h/3

def yYear( year):
    y="윤년" if year%4==0 and year%100 !=0 or year%400==0 else "윤년아님"
    return y
def myabs(a,b):
    a = -1*a if a<0 else a
    b = -b if b<0 else b
    return a+b

def mysum( n ):
    nsum=0
    for i in range(1,n+1):
        nsum = nsum+i # nsum+=i
    return nsum

rst = mysum(5) #hap( 10,20 )
print( rst )


# rst = myabs(-10,20) #hap( 10,20 )
# print( rst )

# rst = yYear(2018) #hap( 10,20 )
# print( rst )

# rst = coneVolume(4,10) #hap( 10,20 )
# print( rst )

# rst = cylinderVolume(4,10) #hap( 10,20 )
# print( rst )

# rst = mToMile(300) #hap( 10,20 )
# print( rst )

# rst = circle_area(3) #hap( 10,20 )
# print( rst )

# rst = gop(10,20) #hap( 10,20 )
# print( rst )
