# duck typing

class School:
    def __init__(self, name):
        self.name = name
        self.names_list = []

    def add_student(self, student):
        self.names_list.append(student)
    
    def students_list(self):
        return[f"  name: {student.name}, age: {student.age}" for student in self.names_list]
    
        
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    
school  = School("new york school")

student = Student("sofia", 17)
student2 = Student("lizi", 16)
student3 = Student("tako", 17)
student4 = Student("mari", 17)


school.add_student(student)
school.add_student(student2)
school.add_student(student3)
school.add_student(student4)

print(school.name)   
for student in school.students_list():
    print(student)