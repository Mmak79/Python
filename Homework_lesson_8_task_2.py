class PositiveCheck(Exception):
    def __init__(self, txt):
        self.txt = txt


class ZeroCheck(Exception):
    def __init__(self, txt):
        self.txt = txt


class Exit(Exception):
    def __init__(self, txt):
        self.txt = txt
        print(self.txt)
        exit(0)


print("* Для завершения программы, введите 'е'")
while True:
    inp_data_1 = input("Введите положительное число (делимое): ")
    if inp_data_1 == "e" or inp_data_1 == "е":
        raise Exit("Программа завершена")
    inp_data_2 = input("Введите число (делитель): ")
    try:
        inp_data_1 = int(inp_data_1)
        if inp_data_1 < 0:
            raise PositiveCheck("Вы ввели отрицательное число!")
        inp_data_2 = int(inp_data_2)
        if inp_data_2 == 0:
            raise ZeroCheck("Делить на ноль нельзя!")
    except ValueError:
        print("Вы ввели не число")
    except PositiveCheck as err:
        print(err)
    except ZeroCheck as zerr:
        print(zerr)
    else:
        print(f"Результат деления: {round(inp_data_1 / inp_data_2, 2)} ")
