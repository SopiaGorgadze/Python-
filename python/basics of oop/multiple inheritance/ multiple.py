# multiple inheritance
#

# multiple inheritance inherits from more than one parent class
#               c(A, B)

# so it means that child class gets all the attributes from multiple parents


# multiple inheritance is when a class inherits from more than one parent class. This means that the child class can access the attributes and methods of both parent classes. This can be useful when you want to create a class that has the functionality of multiple classes.


# class Watch:
#     def show_time(self):
#         print("showing time....")



# class Phone:
#     def make_call(self):
#         print("making a call...")

# class Smartwatch(Watch, Phone):
#     pass


# sw = Smartwatch()
# sw.show_time()
# sw.make_call()





class Prey:
    def flee(self):
        print("this animal is fleeing")

class Predator:
    def hunt(self):
        print("this animal is huntinh")

# rabbit inherited from only prey

class Rabbit(Prey):
    pass

# hawk inherited from only predator

class Hawk(Predator):
    pass

# fish inherited ftom both prey and predator because it can be both

class Fish(Prey, Predator):
    pass


rabbit = Rabbit()

rabbit.flee()
# ======
hawk = Hawk()

hawk.hunt()
# ======
fish = Fish()

fish.flee()
fish.hunt()
# ======