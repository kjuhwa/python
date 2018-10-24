#일급함수: 함수에대해 할당,리턴, 인자, 함수안에 함수

def fn():
    print('fn call')
fn()
print(id(fn))
fn1 = fn #shallow copy
print(id(fn1))
fn1()

#코드세그먼트 텍스트영역에 할당된 함수의 시작주소로 이동
#코드세그먼트 텍스트영역에 할당된 함수의 시작주소
