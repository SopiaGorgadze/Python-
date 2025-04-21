class Fish:

    total = 0 
    def __init__(self, name, color):
        self.name = name
        self.color = color
        Fish.total += 1
    
    # we call this method when an object is deleted so its a delete method and it doesnt need parameters like name and color
    def __del__(self):
 
        Fish.total -= 1
        print(f"{self.name} the fish has been deleted.")
    



fish1 = Fish("bluey", "blue")
fish2 = Fish("goldie", "gold")

print(Fish.total)

del fish1

print(Fish.total)