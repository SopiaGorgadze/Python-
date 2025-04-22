class Cat:
    cat_count = 0

    def __init__(self, name, color):
        self.name = name
        self.color = color
        Cat.cat_count += 1

 

cat1 = Cat("garfield", "orange")
cat2 = Cat("Tommy", "grey")
cat3 = Cat("nigga", "black")

print(Cat.cat_count)