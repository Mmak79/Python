class Cell:
    def __init__(self, i):
        if i > 0:
            self.nucleus = round(i)
        else:
            try:
                raise Exception("Количество клеток должно быть больше 0")
            except Exception as err:
                print(err)
                self.nucleus = False

    @property
    def show(self):
        return self.nucleus

    @property
    def make_order(self):
        if self.nucleus:
            st = self.nucleus // 5
            l_st = self.nucleus % 5
            f_st = "*****\n"
            return f"{f_st * st}{'*' * l_st}"
        return f"Клетки не существует"

    def __add__(self, other):
        new_cell = self.nucleus + other.nucleus
        self.nucleus = 0
        other.nucleus = 0
        return Cell(new_cell)

    def __sub__(self, other):
        new_cell = Cell(self.nucleus - other.nucleus)
        if new_cell.show:
            self.nucleus = 0
            other.nucleus = 0
            return new_cell
        else:
            return False

    def __mul__(self, other):
        new_cell = Cell(self.nucleus * other.nucleus)
        if new_cell.show:
            self.nucleus = 0
            other.nucleus = 0
            return new_cell
        else:
            return False

    def __truediv__(self, other):
        new_cell = Cell(self.nucleus // other.nucleus)
        if new_cell.show:
            self.nucleus = 0
            other.nucleus = 0
            return new_cell
        else:
            return False


cell_1 = Cell(4.3)
cell_2 = Cell(17)
cell_3 = cell_2 + cell_1
print(cell_3.make_order)
print(cell_2.make_order)
