# introduction to inheritance

# inheritance is a way to create a new class based on an existing class
# the new class is called the child class or subclass
# the existing class is called the parent class or superclass
# the child class inherits all the attributes and methods of the parent class
# this means that the child class can use all the methods and attributes of the parent class without having to rewrite them
# this is useful because it allows us to create a new class that has all the functionality of the parent class, but also has its own unique attributes and methods

 
# helps with code reusability and extensibility

# The parent class contains common properties and methods. 

class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


# to inherit we need to add the inheritance list the parenthess and the class were inheriting from

class Dog(Animal):
    def speak(self):
        print("woof")


class Cat(Animal):
    def speak(self):
        print("meow")


class Mouse(Animal):
    def speak(self):
        print("squeak")


# even tho theres nothing in this classes we still have attributes and methods from the parent element


# this is convinient because we dont have to copy and paste all the attributes and elements to each class we can just make them inherit from the parent. its a lot easier for reusing a code


dog = Dog("mimi")

cat = Cat("garfield")

mouse = Mouse("mickey")


print(dog.name)
print(dog.alive)
dog.eat()
dog.sleep()
dog.speak()

print(cat.name)
print(cat.alive)
cat.eat()
cat.sleep()
cat.speak()

print(mouse.name)
print(mouse.alive)
mouse.eat()
mouse.sleep()
mouse.speak()