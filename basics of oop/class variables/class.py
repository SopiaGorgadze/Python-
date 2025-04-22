# class variables


# class variables are shared among all instances of a class, meaning that if one instance changes the value of a class variable, all other instances will see that change.
# class variables are defined outside of the constructor and are shared among all instances of the class.
# instance variables are unique to each instance of a class, meaning that if one instance changes the value of an instance variable, other instances will not see that change.
# instance variables are defined inside the constructor and are unique to each instance of the class.
 
 

# objects created from a class are called instances




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