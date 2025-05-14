# polimorphism, inheritance

class Shape:
    def area(self):
        print( "not implemented")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(self.side ** 2)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print(3.14 * self.radius **2)


shape = Shape()
square = Square(10)
circle = Circle(5)

square.area()
circle.area()
