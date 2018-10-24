def fn():
    my=[10,20,30]
    print(my,'myid', id(my))
    return my

def fn1( a ):
    print(a)

my1 = fn()
print( my1,'my1 id', id(my1) )

fn1( 100 )
fn1( 3.14 )
fn1( [10,20,30] )




#RC( Reference Count:참조계수기법)
# my=[10,20,30]
# my1 = my
# my ='abc'
