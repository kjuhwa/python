g = 10 #전역변수
def fn():
    global g
    g = 100 #지역변수

#fn 코드세그먼테할당된함수의시작주소로 이동
fn()
print('g=', g )
