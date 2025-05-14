# multilevel inheritance

class Person:
    def introduce(self):
        print("hi im a person")

class Student(Person):
    def study(self):
        print("im studying")

class Highschool(Student):
    def attendance(self):
        print("attending high school classes")



school = Highschool()

school.introduce()
school.study()
school.attendance()
#