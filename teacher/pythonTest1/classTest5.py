
class Circle:
    @staticmethod
    def circle_area(r):
        return r**2*3.14

    @staticmethod
    def cylinder_area(r,h):
        return r**2*3.14*h

class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age
print( Circle.circle_area(5))
print( Circle.cylinder_area(5,10))
data =[]
data.append( Student('홍길동',20) )
data.append( Student('이순신',30) )
for dt in data:
    print( dt.name, dt.age)

# std1 = Student('홍길동',20)
# #std1.__init__(std1,'홍길동',20)
# print(std1.name, std1.age)
# std2 = Student('이순신',30)
# #std1.__init__(std1,'홍길동',20)
# print(std2.name, std2.age)



