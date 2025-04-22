# multilevel inheritance


class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"hi im a {self.name}")

class Student(Person):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def study(self):
        print(f"im studying {self.subject}")

class Highschool(Student):
    def __init__(self, name, subject, attendanc):
        self.name = name
        self.subject = subject
        self.attendanc = attendanc
    def attendance(self):
        print(f"{self.attendanc} high school classes")



school = Highschool("sofia", "physics", "not attending")

school.introduce()
school.study()
school.attendance()
#