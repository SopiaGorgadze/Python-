# type function

# type() function in python indicates the type of variable/object
x = 10
y = "sophia"

print(type(x))
print(type(y))


# id function

# id() function provides the adress of variable/object, its a memory adress. this id is unique and constant

a = 10
b = 10

print(id(a))
print(id(b))

print(id(x) == id(b))  #true


# if we make different variables but the values are the same, the adresses will be the same too. 

# this happens because Python checks if an identical immutable object already exists in memory, and if so it reuses instead of creating a new one

# this is called "intering" or "object reuse" it saves memory and speeds up the performance










