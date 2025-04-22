# multiple inheritance


# method resolution order (MRO)

class Painter:
    def create(self):
        print("painting a beautiful landscape")

class Poet:
    def create(self):
        print("writing a deep poem")


# i switched this parameters and if the poet was first one "writing a deep poem" printed and if the painter was first "painting a beautiful landscape" printed  ---->>> method resolution order (MRO).
class Creative(Poet, Painter):
    pass

ct = Creative()
#
ct.create()