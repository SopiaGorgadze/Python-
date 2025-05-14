# composition

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []

    def add_students(self, student):
        self.students.append(student)
    
    def student_list(self):
        for student in self.students:
            print(student.name)


student = Student("andria", 17)
student2 = Student("tako", 17)
student3 = Student("blabla", 17)

school = School("new york school")


school.add_students(student)
school.add_students(student2)
school.add_students(student3)

school.student_list()