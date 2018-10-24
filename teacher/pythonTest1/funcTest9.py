a=10
b=3.14
c='abc'
t =(10,20,30)
s = 'a={0} b={1} c={2}'.format( a,b,c )
# s = 'a={} b={} c={}'.format( a,b,c )
# s = 'a=%d b=%f c=%s'%(a,b,c)
# s = f'a={a} b={b} c={c}'
print(s)
s1 = '{0:10} {1} {2}'.format( *t )
print(s1 )
s2 = '{aa} {bb} {cc}'.format( aa=100,bb=200,cc=300)
print(s2)
d ={'name':'홍길동','age':20}
s3 ='이름:{name} 나이:{age}'.format(**d )
print(s3)
