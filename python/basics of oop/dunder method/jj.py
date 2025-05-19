# dunder method

class Temp:
    def __init__(self, celsius):
        self.celsius = celsius

    def __int__(self):
        return int(self.celsius)


temp1 = Temp(50.0)

print(int(temp1))
