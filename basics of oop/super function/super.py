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

    def describe(self):
        # ternary operator
        print(f"it is {self.color} and {'filled' if self.filled else 'not filled'}")



class Circle(Shape):
    # within a child class we also can use constructor method to assign attributes 
    def __init__(self, color, filled, radius):
        # dunder init method
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        print(f"it is a circle with an area of {3.14 * self.radius * self.radius}")
        super().describe()  # we extended the method right here

    # this is called method overriding if a child shares a similar method as a parent we will use the childs method and not the parents, if we want to extend functionality of a child element we will use the super function

class Square(Shape):
    def __init__(self, color, filled, width):
    # when we refer to super imagine that were replacing that function with the parrent class name, that makes it more easier to see what does it do
        super().__init__(color, filled)
        self.width = width
    
    def describe(self):
        print(f"it is triangle with an area of {self.width * self.width / 2}")
        super().describe()

class Triangle:
    def _init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height



circle = Circle(color = "red",filled =  True, radius = 5)

print(circle.color)
print(circle.filled)
print(circle.radius)


square = Square(color = "blue", filled = True, width = 20)

print(square.color)
print(square.filled)
print(square.width)
 
circle.describe()

square.describe()