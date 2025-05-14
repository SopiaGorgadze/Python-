# polimorphism, inheritance

class Employee:
    def work(self):
        print("working..")

class Manager(Employee):
    def work(self):
        print("managing team and projects")

class Developer(Employee):
    def work(self):
        print("writing and debugging code")

employee = Employee()
manager = Manager()
developer = Developer()

team = [manager, developer]

for employee in team:
    employee.work()