class Worker:
    def __init__(self, n, s_n, p, wage, bonus):
        self.name = n
        self.surname = s_n
        self.position = p
        self._income = {"wage": wage, "bonus": bonus}


class PositionDir(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


x = PositionDir("Maria", "Makarenko", "dir", 25000, 9000)
print(x.get_full_name())
print(x.get_total_income())
