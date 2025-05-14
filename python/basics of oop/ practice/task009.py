# inheritance

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self,name, position, salary, department="hr"):
        self.name = name
        self.position = position
        self.salary = salary
        self.department = department
    
    def manage(self):
        print(f"Managing the {self.department} department.")

class Developer(Employee):
    def __init__(self,name, position, salary, programming_language = "pythonr"):
        self.name = name
        self.position = position
        self.salary = salary
        self.programming_language = programming_language

    def code(self):
        print(f"Writing code in {self.programming_language}.")

#

class Designer(Employee):
    def __init__(self,name, position, salary, design_tool= "figma"):
        self.name = name
        self.position = position
        self.salary = salary
        self.design_tool = design_tool

    def design(self):
        print(f"designing with {self.design_tool}")



manager = Manager("alice", "manager", 8000)
developer = Developer("sopia", "developer", 20000)
designer = Designer("charlie", "designer", 1010101)

print("-" * 30)
 
manager.manage()
manager.info()

print("-" * 30)

developer.code()
developer.info()

print("-" * 30)

designer.design()
designer.info()