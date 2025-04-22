# object oriented programming

# object oriented programming is a programming paradigm that uses objects and classes to structure code. it allows for the creation of reusable and modular code, making it easier to manage and maintain large codebases.
# it is a way of organizing code that is based on the concept of objects. an object is a self-contained unit that contains both data and methods that operate on that data. this allows for the creation of complex data structures and the ability to model real-world entities in code.

# object - a bundle of related attributes which can represent real life things just like phone, cup or book
 #


# class is used to design structure and layout of the object.
# to create a class we must write class and then a related name of what object we are about to create, this name is just like a variable
class car:
    # this method is called constructor it works similarly as function. to define this function we need __init__(self), init means initialise . this is a constructor method also caled dunder method. dunder is double underscores -> __init__(self) followed buy parenthes. 


    # as we know this method behaves like function so we need set of parameters. attributes
    # 
    # self means this object were creating right now. so this car that im creating 
    # 
    def __init__(self, model, year, color, for_sale): 
        # to assign these attributes we need self
        # when we get a set of parameters we will asign them to these objects 
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # this is how we define methods in a class

    # methods are functions that belong to a class. they are used to define the behavior of an object. methods can access and modify the attributes of an object, allowing for encapsulation and data hiding.
    # methods are defined using the def keyword, just like functions, but they must always include self as the first parameter. this allows methods to access the attributes and other methods of the object they belong to.
    def drive(self):
        print(f"you drive the car {self.color} {self.model}")

    def stop(self):
        print(f"you stop the car {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


# objects are instances of a class. when we create an object, we are creating an instance of a class. this means that the object has all the attributes and methods of the class, but it also has its own unique values for those attributes. this allows for the creation of multiple objects from the same class, each with its own unique data.
# to create an object from a class, we simply call the class name followed by parentheses. this will call the constructor method and create a new object with the specified attributes. like this:
# car1 = car("subaru", 2015, "green", False)