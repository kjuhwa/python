def fn1():
    return 10,20

rst = fn1()
print(rst)

a,b = fn1()
print(a,b)

def shape(r, h,w):
    return r**2*3.14, h*w

carea,rectArea = shape(3,10,20)
print(carea,rectArea)

def fn2(a,b):
    print(a,b)

fn2(1,2)
fn2(b=100,a=200) # 명시적 인자호출

def fn3(a=10,b=20,c=30): # 디폴트 인자
    print(a,b,c)

fn3()
fn3(100)
fn3(100,200)
fn3(100,200,300)
fn3(b=1000)

print(10,20,sep='-')
print('hello',end=' ')
print('korea')
