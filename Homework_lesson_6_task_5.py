class Stationery:
    title = "project"

    def draw(self):
        print(f"{self.title} start rendering")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title} start rendering pen")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} start rendering pencil")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} start rendering handle")


s = Stationery()
s.draw()

p = Pen()
p.draw()

p_l = Pencil()
p_l.draw()

h = Handle()
h.draw()
