class StrCheck(Exception):
    def __init__(self, txt):
        self.txt = txt


class Exit(Exception):
    def __init__(self, txt, ls):
        self.txt = txt
        print(self.txt)
        print(ls)
        exit(0)


registry = []
print("* Для завершения программы, введите 'stop'")
while True:
    try:
        new_num = input("Введите число: ")
        if new_num == "stop":
            raise Exit("Завершение работы программы", registry)
        new_num = int(new_num)
        registry.append(new_num)
    except ValueError:
        try:
            raise StrCheck("Строковые значения не принимаются")
        except StrCheck as str_err:
            print(str_err)
