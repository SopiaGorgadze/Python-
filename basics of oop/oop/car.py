# object oriented programming

# object - a bundle of related attributes which can represent real life things just like phone, cup or book
 


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

    def drive(self):
        print(f"you drive the car {self.color} {self.model}")

    def stop(self):
        print(f"you stop the car {self.color} {self.model}")


    def describe(self):
        print(f"{self.year} {self.color} {self.model}")