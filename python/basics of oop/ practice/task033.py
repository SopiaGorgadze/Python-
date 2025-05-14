# composition


class Driver:
    def __init__(self,name):
        self.name = name

class Car:
    def __init__(self, model, driver):
        self.nodel = model
        self.driver = driver 
    

    def drive(self):
        print(self.driver.name)


driver = Driver("luka")

car = Car("tesla", driver)

car.drive()