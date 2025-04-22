# abstract class: 

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        print(self.width * self.height)


    def perimeter(self):
        print(2 * (self.width + self.height))
        




rect = Rectangle(11, 2)

rect.area()
rect.perimeter()