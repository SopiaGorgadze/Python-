# nested class 

# A nested class is a class defined inside another class

# what nested classes are good for:
# 1. grouping related things together
# 2. keeping code cleaner and more organized
# 3. avoiding name clashes
#  (If two different parts of your program need a class with the same name, nesting them can prevent confusion.)


# When NOT to use them:
# 1. If the inner class is going to be used outside the outer class.
# 2. f it makes things harder to read for no good reason.

# class Employee:
#     print("this is the first class")


# class Employee:
#     print("this is the second class")

# now we have a naming conflict we have same classes with the same names, if we run this program we will execute both classes.

# but we could write something like this

class Company:
    class Employee:
        print("this is the first class")

class Nonprofit:
    class Employee:
        print("this is the second class")

# we can have two classes with the same names as long as they are in different scopes