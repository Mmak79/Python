from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        self.all = []

    @property
    def _sum(self):
        s = sum(self.all)
        return s

    @property
    def cleanup(self):
        self.all = []
        return self.all

    def __add__(self, other):
        return round(self._sum + other._sum, 2)

    @abstractmethod
    def cloth(self, a):
        pass

    def cons(self, x, y=1):
        c_1 = self.cloth(x) * y
        self.all.append(c_1)


class Coat(Clothes):
    def cloth(self, v):
        consumption_coat = v / 6.5 + 0.5
        return consumption_coat


class Costume(Clothes):
    def cloth(self, h):
        consumption_cost = 2 * h + 0
        return consumption_cost


coat = Coat()
coat.cons(52, 10)
coat.cons(48, 15)
coat.cons(45, 5)

cost = Costume()
cost.cons(1.7, 10)
cost.cons(2, 4)
cost.cons(2.1, 2)
print(f"Общий расход ткани: {cost + coat}")
