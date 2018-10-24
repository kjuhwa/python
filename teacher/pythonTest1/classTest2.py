# 동일한 클래스에서 여러개의 객체가 생성된경우
# 멤버데이터는 메모리별도영역 할당되지만
#멤버함수는 공유한다(코드) 그런데
#어떻게 각각의 멤버데이터영역에 값을 W/R
# self에의해 가능하다
class Test:
    def __init__(self):
        print('constructor call')
        self.a =0
        self.b =0
    def setData( self, x, y):
        print( 'self id', id(self))
        self.a = x
        self.b = y
obj = Test()
print( 'obj id', id(obj))
obj.setData(100,200)
print( obj.a, obj.b )

obj1 = Test()
print( 'obj1 id', id(obj1))
obj1.setData(10,20)
print( obj1.a, obj1.b )
