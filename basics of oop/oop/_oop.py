from car import car

# we need a matching set of arguments
car1 = car("subaru", 2015, "green", False)
car2 = car("bmw", 2025, "red", True)

# print(car2.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)

car1.drive()

car1.stop()

car2.describe()