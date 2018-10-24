#파이썬 접근권한자 (public)
# 클래스의 멤버데이터메모리할당이완료(객체생성)
class Test:
    def __init__(self):#생성자 함수(객체생성시 자동호출)
        print('constructor call')
        self.a =0
        self.b =0

    def setData( self, x, y):
        print( 'self id', id(self))
        self.a = x
        self.b = y

obj = Test() #obj.__init__(obj) #new Test()(자바와 같은의미)
print( 'obj id', id(obj))
obj.setData(100,200) #obj.setData(obj, 100,200)
print( obj.a, obj.b )
