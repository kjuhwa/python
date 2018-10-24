class Test:
    def __init__(self):
        print('constructor call')
        self.a = 0
        self.b = 0

    def __del__(self):
        print('dest call')

    def setData(self, x, y ):
        self.a = x
        self.b = y

    def show(self):
        print(self.a, self.b)

def fn():
    obj = Test()
    obj.show()
    return obj

my = fn()
print('hello')

# obj = Test()
# my = obj
# obj.setData(10,20)
# obj.show()
# obj = 'abc'
# print('hello')
