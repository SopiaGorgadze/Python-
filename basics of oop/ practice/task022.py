# super()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    # override
    def speak(self):
 
        super().speak()
        print(f"{self.name} barks")


dog = Dog("mimi")

dog.speak()