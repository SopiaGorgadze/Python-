#  2. "Duck typing" is another way to achieve polymorphism in python besides inheritance. object must have necessary attributes/methods
# """
# This script demonstrates the concept of "Duck Typing" in Python.

# Duck Typing is a programming concept related to dynamic typing, where the type or class of an object is less important than the methods and properties that the object has. 
# The name comes from the saying, "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

# In Python, Duck Typing allows you to write more flexible and reusable code by focusing on the behavior of objects rather than their specific types.
# """


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")


class Car:
    alive = False
    def horn(self):
        print("honk")
# The Car class does not inherit from Animal, but it has a method called horn. but it can be used in the same way as the Animal classes.
    def speak(self):
        print("honk")
# The Car class has a method called speak, which is similar to the speak method in the Animal classes
# this is an example of duck typing, where the type of the object is not important as long as it has the required method.

animals = [Dog(), Cat() ,Car()]

# In this example, both Dog and Cat classes have a speak method.

for animal in animals:
    animal.speak()
#

