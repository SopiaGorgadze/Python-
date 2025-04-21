# inheritance

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self.running = False

    def start(self):
        self.running = True
        print(f"The {self.brand} is now running")
    
    def stop(self):
        self.running = False
        print(f"The {self.brand} has stopped")
    

class Car(Vehicle):
    def honk(self):
        print("beep")


class Motorcycle(Vehicle):
    def honk(self):
        print("vroom")


class Truck(Vehicle):
    def honk(self):
        print("honk")

car1 = Car("toyota"
)
moto = Motorcycle("Bmw")

truck = Truck("tesla")

print(car1.brand)
print(moto.brand)
print(truck.brand)

car1.honk()

moto.honk()

truck.honk()