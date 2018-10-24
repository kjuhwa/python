#파이썬이 자동붙여주는 전역변수
g = 10 #전역변수
def fn():
    g = 100 #지역변수
    print( locals() )

fn()
print('g=', g )
print( globals() ) #전역변수
print(__file__)
