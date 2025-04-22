# super()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"hello my name is {self.name} my age is {self.age}")

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def greet(self):
        print(f"hello my name is {self.name} my age is {self.age} my school is {self.school}")

person = Person("sofia", 17)
student = Student("sofia", 17, "highschool")

person.greet()
student.greet()
#