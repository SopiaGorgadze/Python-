# class variables


# class  = shared among all of the objects created from a class (instances) which are defined inside a constructor 
# class variables are defined outside a constructor, class variables allow us to share data among all objects created from the class. 

# with instance variables each object has their own version
# with the class variable all those objects share one variable
 

class Student:

    class_year = 2026
    num_students = 0

    def __init__(self, name, age):

        # instance variables
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("sofia", 17)

student2 = Student("levani", 30)

student3 = Student("tea", 47)


# its good practice to access the class variable by the class name

print(f"my graduating class of {Student.class_year} has {Student.num_students} students")

print(student1.name)
print(student2.name)
print(student3.name)