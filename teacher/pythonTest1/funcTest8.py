def fn(*args): #가변인자(인자의 갯수가 고정이 아니다)
    print(args)

def circles( *rs ):
    for r in rs:
        print( r**2*3.14 )

def fn1(**kwargs): #정의되지않은인자
    print( kwargs)

# def fn2( *args,a ): #반드시 가변인자는뒤에X
def fn2( a, *args ): #반드시 가변인자는뒤에
    print(a)
    print(args)
#일반인자--> 가변인자 -->정의되지않은인자
def fn3( *args, **kwargs):
    print(args)
    print(kwargs)

fn3( 10,20,30 )
fn3(10,20,30,aa=10,bb=20)
fn3(aa=10,bb=20,cc=30)


# fn2(10,20,30,40)
# d ={'name':'이순신','age':30}
# fn1(aa=10,bb=20)
# fn1(name='홍길동',age=20)
#fn1( **d) # fn1(name='이순신',age=30)



# fn( *(1,2,3,4) )
# fn(1,2,3,4 )

# circles(1,2,3,4,5)

# rst = (10+2)*3
# a = (10) # 연산자우선순위,튜플
# print(a, type(a) )
# fn(10,20,30)
# fn(1,2,3,4,5,6)
