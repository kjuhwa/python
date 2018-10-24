def fn():
    my=[10,20,30]
    print(my,'myid', id(my))
    return my

def fn1( a ):
    print(a)

# my1 = fn()
# print( my1,'my1 id', id(my1) )

# fn1( 100 )
# fn1( 3.14 )
# fn1( [10,20,30] )

for n in range(1,11):
    if 10%n==0:
        print(n)

def yaksu(num):
    y = []
    for n in range(1, num+1):
        if num%n==0:
            y.append(n)
    return y

rst = yaksu(10)
print(rst)



#RC( Reference Count:참조계수기법)
# my=[10,20,30]
# my1 = my
# my ='abc'
