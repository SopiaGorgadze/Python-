class Bird:

    bird_count = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Bird.bird_count += 1

    def chirp(self):
        print(f"Tweet! I'm {self.name} the {self.species}.")

bird1 = Bird("chiti", "chiti")
bird2 = Bird("chiti", "chiti")
bird3 = Bird("chiti", "chiti")
bird4 = Bird("chiti", "chiti")

bird1.chirp()
print(Bird.bird_count)




    #