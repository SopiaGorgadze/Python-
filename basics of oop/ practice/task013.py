
class Prey:
    def flee(self):
        print("this animal is fleeing")

class Predator:
    def hunt(self):
        print("this animal is huntinh")
 
class Rabbit(Prey):
    pass
 
class Hawk(Predator):
    pass
 

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
# ======#