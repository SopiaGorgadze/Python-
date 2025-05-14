# abstract class: 
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


    @abstractmethod
    def perimeter(self):
        pass
#

class Circle(Shape):
    def __init__(self, pi, radius):
        self.pi = pi
        self.radius = radius
    def area(self):
        print(self.pi * self.radius**2)

    def perimeter(self):
        print(2 * self.pi * self.radius)

circle = Circle(3.14, 7)

circle.area()
circle.perimeter()