# abstract class: 

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Triangle(Shape):
    def __init__(self, a, b, fudze, height):
        self.a = a
        self.b = b
        self.fudze = fudze
        self.height = height

    def perimeter(self):
        print(self.a + self.b + self.fudze)

    def area(self):
        print(0.5 * self.fudze * self.height)


tri = Triangle(10, 12, 20, 9)

tri.perimeter()
tri.area()