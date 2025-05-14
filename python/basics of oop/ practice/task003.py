
class Student:


    count = 0

    def __init__(self, name, grade, gpa):
        self.name = name
        self.grade = grade
        self.gpa = gpa
        Student.count += 1

    def introduce(self):
        print(f"Hi, I'm {self.name}, in grade {self.grade}, and my GPA is {self.gpa}.")

    def honors(self):
        if self.gpa >= 3.5:
            print(True)
        else:
            print(False)


student1 = Student("Levani", "11", 2.0)
student2 = Student("Sofia", "11", 3.8)

print(student1.name)
print(student1.grade)
print(student1.gpa)

print(student2.name)
print(student2.grade)
print(student2.gpa)

student1.introduce()
student1.honors()

student2.introduce()
student2.honors()

print(Student.count)
#