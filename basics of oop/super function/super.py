# super()

# super is a function it is used in child class to call methods from a parent class(superclass)

# it allows us to extend the functionality of the inherited methods


# all of this classes have two attributes in common color and filled, and in programming we always try not to repeat ourselves if we dont have to

# if we had to make any changes to repeated attributes we would have to do this manually which is very hard



# class Circle:
#     def _init__(self, color, filled, radius):
#         self.color = color
#         self.filled = filled
#         self.radius = radius

# class Square:
#     def _init__(self, color, filled, width):
#         self.color = color
#         self.filled = filled
#         self.width = width


# class Triangle:
#     def _init__(self, color, filled, width, height):
#         self.color = color
#         self.filled = filled
#         self.width = width
#         self.height = height


# soo instead of this big code we can write

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled



class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width


class Triangle:
    def _init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height



circle = Circle(color = "red",filled =  True, radius = 5)

print(circle.color)
print(circle.filled)
print(circle.radius)