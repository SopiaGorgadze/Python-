class Employee:
    def work(self):
        print("working..")

class Manager(Employee):
    def __init__(self, name):
        self.name = name
    def work(self):
        print(f"{self.name} is managing team and projects")

class Developer(Employee):
    def __init__(self, name):
        self.name = name
    def work(self):
        print(f"{self.name} is writing and debugging code")

employee = Employee()
manager = Manager("lizi")
developer = Developer("sofia")

team = [manager, developer]

for employee in team:
    employee.work()