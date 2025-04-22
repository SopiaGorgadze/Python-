# super()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id


emp = Employee("sofia", 17, 0)

print(emp.name)

print(emp.age)

print(emp.id)