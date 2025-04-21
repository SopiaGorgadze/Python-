# inheritance - allows class to inherit attributes and methods from another class
# helps with code reusability and extensibility

class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass


class Cat(Animal):
    pass

class Mouse(Animal):
    pass


dog = Dog("mimi")

cat = Cat("garfield")

mouse = Mouse("mickey")


print(dog.name)
print(dog.alive)
dog.eat()
dog.sleep()