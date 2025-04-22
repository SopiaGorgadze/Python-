# abstract class: 

# an abstract class is a class that can not be created on its own and is meant to be inherited by ither classes. theyre supposed to be parent classes. 

# abstract base classes
from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the car")

    def stop(self):
        print("you stop the car")

class Moto(Vehicle):
    def go(self):
        print("you ride the motorcycle")

    def stop(self):
        print("you stop the motorcycle")

class Boat(Vehicle):
    def go(self):
        print("you sail the boat")

    def stop(self):
        print("you stop sailing the boat")


car = Car()

car.go()
car.stop()

moto = Moto()
moto.go()
moto.stop()

boat = Boat()
boat.go()
boat.stop()