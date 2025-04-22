# multilevel inheritance


# multilevel inheritance inherits from a parent which inherits from another parebt

#           C(B) <-- B(A)  <-- A
#           Grandparent class --> Parent class --> Child class

# multilevel inheritance is when a class inherits from a parent class, which in turn inherits from another parent class. This means that the child class can access the attributes and methods of both parent classes. This can be useful when you want to create a class that has the functionality of multiple classes.

class Animal:
    # when we add a constructor in the biggest parrent we dont need to asign constructors and  attributes to child classes 
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is huntinh")

 

class Rabbit(Prey):
    pass
 

class Hawk(Predator):
    pass
 
class Fish(Prey, Predator):
    pass


rabbit = Rabbit("bugs")

rabbit.flee()

rabbit.eat()
rabbit.sleep()
# ======
hawk = Hawk("tony")

hawk.hunt()


hawk.eat()
hawk.sleep()
# ======
fish = Fish("nemo")

fish.flee()
fish.hunt()


fish.eat()
fish.sleep()
# ======
