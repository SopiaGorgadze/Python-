# Composition in Python means creating classes that use other classes to build complex functionality. It’s like saying, “A car has a engine” instead of “A car is a vehicle” (which would be inheritance).

# composition the composed object directly owns its components, which can not exist independently

# a little example


class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self):
        self.engine = Engine()  #so here we see that car class has engine class and thats the whole composition

    def drive(self):
        self.engine.start()
        print("Car is driving.")



# class Engine:
#     def __init__(self, horse_power):
#         self.horse_power = horse_power

# class Wheel:
#     def __init__(self, size):
#         self.size = size


# class Car:
#     def __init__(self, make, model, horse_power, wheel_size):
#         self.make = make
#         self.model = model
#         self.engine = Engine(horse_power)
#         self.wheel = [Wheel(wheel_size) for wheel in range(4)] 

#     def display_car(self):
#         return f"{self.make} {self.model} {self.engine.horse_power}  {self.wheel[0].size}"


# car = Car(make = "ford", model = "mustang", horse_power =500, wheel_size = 18)
# car2 = Car("chevrolet", "corvette", 670, 19)



# print(car.display_car())

# print(car.display_car())