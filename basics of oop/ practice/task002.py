class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.brand} is starting")

    def stop(self):
        print(f"{self.brand} is stopping")

    def desc(self):
        print(f"this is a {self.year} {self.brand} {self.model}")


car1 = Car("subaru", "Crosstrek", 2015)

print(car1.brand)
print(car1.model)
print(car1.year)

car1.start()
car1.stop()
car1.desc()
#