# 파이썬이 자동으로 붙여주는 전역변수
g = 10 #전역변수
def fn():
    g = 100 #지역변수
    print(locals())

fn()
print('g=', g )
print(globals())
print(__file__)
