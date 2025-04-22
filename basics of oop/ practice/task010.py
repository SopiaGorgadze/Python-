# multiple inheritance


class Artist:
    def draw(self):
        print("Drawing a sketch")


class Musician:
    def play(self):
        print("playing music")

class Performer(Artist, Musician):
    pass

performer = Performer()

performer.draw()
performer.play()
#