def fn1():
    return 10,20

def shape(r, h,w):
    return r**2*3.14, h*w

def fn2(a,b):
    print(a,b)

def fn3(a=10,b=20,c=30): #디폴트 인자
    print(a,b,c)

# fn3()
# fn3(100)
# fn3(100,200)
# fn3(100,200,300)
# fn3(b=1000)

print(10,20, sep='-')
print('hello',end=' ')
print('korea')
# fn2(10,20)
# fn2(b=100,a=200) #명시적 인자호출


# carea,rectArea = shape(3,10,20)
# print( carea, rectArea )
# print(rst )

# a,b = fn1()
# print(a,b)
# rst = fn1()
# print( rst )
