# 모든 클래스는 기본적으로 object
class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def show(self):
        print(self.a, self.b)
    #오버라이딩 (object)
    def __repr__(self):
        return 'a=%d b=%d'%(self.a,self.b)

obj = Test(100,200)
obj.show()
print(obj) #obj.__repr__()

