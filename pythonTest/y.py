a = 10
b = 3.14
c = 'abc'
# s = 'a=%d b=%f c=%s'%(a,b,c)
s = 'a=%5d b=%10.2f c=%10s'%(a,b,c)
print(s)

d = {'name':'홍길동','age':20,'addr':'서울시'}
s1 = '이름:%(name)s 나이:%(age)d 주소:%(addr)s'%d
print(s1)
s2 = f'a={a:10}, b={b}, c={c}'
print(s2)
