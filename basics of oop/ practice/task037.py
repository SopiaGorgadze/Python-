# nested classes



# The outer class should be called School.
# The nested class should be called Student.
# The Student class should have:
# name and grade as attributes.
# A method greet() that prints a greeting message with the student's name and grade.
# The School class should have a method display_students() that lists all students in the school (you can store them in a list).
# 🧠 Bonus (optional):

# Add a method in the School class that prints out the number of students.


class School:
    def __init__(self):
        self.student_list = []
        self.student_grades = []

    def display(self):
        for student in self.student_list:
            print(f"NAME: {student}")

        for grade in self.student_grades:
            print(f"GRADE: {grade}")

    def count(self):
        print(f"student count : {len(self.student_list)}")

    class Student:
        def __init__(self, name, grade):
            self.name = name
            self.grade = grade

        
            
        def greet(self):
            print(f"hello {self.name} your grade is {self.grade}")
            school.student_list.append(self.name)
            school.student_grades.append(self.grade)
            

school = School()

student = school.Student("sophia", 2)
student2 = school.Student("lizi", 3)
student3 = school.Student("tako", 2)
student4 = school.Student("mari", 1)





student.greet()
student2.greet()
student3.greet()
student4.greet()

school.count()

school.display()

 