class Phone:
    # i created phone class with brand and model
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Person:
    # then i created person class with name and phone
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone #this is where the composition happens

    def call(self):
        print(f"{self.name} is calling from {self.phone.brand} {self.phone.model}") 

phone = Phone("iphone", "12 pro")
person = Person("sophia", phone) #i assign phone object to person object

person.call()