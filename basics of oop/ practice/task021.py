class Logger:
    def __init__(self):
        print("logger is initialisefd")

class User(Logger):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email


us = User("Sofia", "sofiagorgadze@icloud.com")

print(us.name, us.email)

