# polimorphism 
#
# polimorphism is a greek word that means to have "many forms or faces"

#           poly = many
#           morphe = form


#           TWO WAYS TO ACHIEVE POLYMORPHISM 
#           1. inheritance - an object could be  treated of the same as a parent class
#           2. "Duck typing" - object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return self.base * self.height * 0.5


# if the pizza class does not inherit from the shape and we write it into shapes list its gonna come up as an error


# our pizza inherits from a circle class and circle class inherits from a shape class.  so its a pizza a circle and a shape. three in one

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping
   




# since Circle class inherits from the shape class our circle is also considered shape so circle is a circle and also is a shape not a triangle not a square, same goes for other child classes
# circle = Circle()

# a triangle is a triangle and also is a shape because it inherits from a shape class

# triangle = Triangle()

# so if we were about to create a list of shapes it would loook like this

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("peperoni", 10)] 
# if the pizza class does not inherit from the shape and we write it into shapes list its gonna come up as an error


# each of these objects have two forms or two faces


for shape in shapes:
    print(shape.area())


# so this is a polymorphism