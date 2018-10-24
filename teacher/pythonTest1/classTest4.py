#인스턴스(Data용클래스)
#static(데이터처리, 연산용)
class Test:
    st = 100 #정적변수( global(static)영역에)
    def __init__(self):
        print('constructor call')
        self.a =0 #인스턴스 변수(반드시객체생성이필요)
        self.b =0

    @staticmethod
    def setSt(): #정적함수( 인스턴스변수사용불가)
        print('set St function')
        Test.st = 10

    def setData( self, x, y): #인스턴스함수
        self.a = x
        self.b = y
    def show(self):#인스턴스함수
        print( self.a, self.b )
Test.setSt()
print(Test.st )

# obj = Test()
# obj.setData(10,20)


