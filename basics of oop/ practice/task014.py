# multilevel inheritance

class Device:
    def power(self):
        print("device conected to power")

    
class Computer(Device):
    def run(self):
        print("the program is running")


class Laptop(Computer):
    def fold(self):
        print("laptop is folding")


lap = Laptop()

lap.power()
lap.run()
lap.fold()