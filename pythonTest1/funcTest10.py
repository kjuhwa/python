#일급함수 : 함수에대해 할당, 리턴, 인자, 함수안에 함수

def fn():
    print('fn call')

#코드세그먼트 텍스트영역에 할당된 함수의 시작주소로 이동
fn()
print(id(fn))
#코드세그먼트 텍스트영역에 할당된 함수의 시작주소

fn1 = fn # Shallow copy
print(id(fn1))
fn1()
