# polimorphism, inheritance

class Device:
    def start(self):
        print("starting device")

class Laptop(Device):
    def start(self):
        print("laptop is starting")

class Phone(Device):
    def start(self):
        print("phone is turning on")

device = Device()
laptop = Laptop()
phone = Phone()

device.start()
laptop.start()
phone.start()