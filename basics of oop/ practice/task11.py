# multiple inheritance

class Writer:
    def write(self):
        print("writing a story")

class Speaker:
    def speak(self):
        print("giving a speech")

class Author(Writer, Speaker):
    def introduce(self):
        print("i am an author i write and i speak")

au = Author()


au.write()
au.speak()
au.introduce()