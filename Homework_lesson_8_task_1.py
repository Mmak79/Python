class DateOf:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def my_split(cls, data):
        data_1 = data.split("-")
        try:
            d = int(data_1[0])
            m = int(data_1[1])
            y = int(data_1[2])
        except ValueError:
            print("Only int - '01-01-2021'")
            return False
        return cls(d, m, y)

    @staticmethod
    def my_check(el):
        if not el:
            return False
        _try_dict = {1: [range(1, 32), "01"],
                     2: [range(1, 29), "02"],
                     3: [range(1, 32), "03"],
                     4: [range(1, 31), "04"],
                     5: [range(1, 32), "05"],
                     6: [range(1, 31), "06"],
                     7: [range(1, 32), "07"],
                     8: [range(1, 32), "08"],
                     9: [range(1, 31), "09"],
                     10: [range(1, 32), "10"],
                     11: [range(1, 31), "11"],
                     12: [range(1, 32), "12"]}
        if 0 < el.year < 2122:
            if el.month in _try_dict.keys():
                if el.day in _try_dict[el.month][0]:
                    print(f"{el.day}.{_try_dict[el.month][1]}.{el.year}")
                    return True
                else:
                    print("Invalid day")
                    return False
            else:
                print("Invalid month")
                return False
        else:
            print("Invalid year")
            return False


date = input("Введите дату через дефис: ")
sp = DateOf.my_split(date)

while not DateOf.my_check(sp):
    date = input("Введите дату через дефис: ")
    sp = DateOf.my_split(date)
