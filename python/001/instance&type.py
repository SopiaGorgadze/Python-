# difference between instance and type

# ტაიპი ამოწმებს იმას თუ რა ტიპისაა გარკვეული მონაცემი. აი მაგალითად:

x = 10

print(type(x)) #<class 'int'>

# instance კი არის ფუნქცია რომელიც ამოწმებს, არის თუ არა x შექმნილი ინტ კლასისგან აი მაგალითად:

print(isinstance(x, int))


# მთავარი განსხვავება:

# ტიპი გვეუბნება თუ რა მონაცემთა ტიპია x ცვლადი

# და ინსტანსი ამოწმებს არის თუ არა x ცვლადი ინტეჯერის მაგალითი



# task


class Animal:
    pass
class Dog(Animal):
    pass
class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print(type(dog)) #აქ ჩვენ უბრალოდ შევამოწმეთ dog ობიექტის ტიპი

print(isinstance(cat, Animal))  #აქ კი შევამოწმეთ არის თუ არა cat ობიექტი Animal კლასისგან წარმოებული
print(isinstance(dog, Animal))