class Dog:

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print("woof")
    
    def get_info(self):
        print(f"my name is {self.name}, i am {self.age} old {self.breed}")


dog1 = Dog("mimi", "yorkie", 7)


print(dog1.name)
print(dog1.breed)
print(dog1.age)

dog1.bark()

dog1.get_info()
#