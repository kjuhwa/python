
class Circle:

    @staticmethod
    def circle_area(r):
        return r**2*3.14

    @staticmethod
    def cylinder_area(r,h):
        return r**2*3.14*h

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(Circle.circle_area(5))

std1 = Student('홍길동', 20)
print(std1.name, std1.age)
