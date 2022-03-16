class StoreEquipment:
    def __init__(self, compartment):
        self.compartment = compartment
        self.stor = {}

    @property
    def me(self):
        return self.compartment

    @property
    def total_cost(self):
        t_cost = 0
        for el, c in self.stor.items():
            t_cost += el.cost * c
        return t_cost

    @property
    def state(self):
        if not self.stor:
            print(f"на складе {self.compartment} пусто")
            return False
        return self.stor

    @property
    def inventory(self):
        remove = []
        for k, v in self.stor.items():
            if v == 0:
                remove.append(k)
        for k in remove:
            self.stor.pop(k)
        return self.state

    def move_in_store(self, _type, _count):
        if _type in self.stor.keys():
            self.stor[_type] += _count
        else:
            self.stor[_type] = _count
        return self.stor

    def move_out_store(self, _type, _count):
        if _count <= 0:
            print(f"нельзя попросить {_count} {_type.__name__}")
            return False
        if _type in self.stor.keys():
            if self.stor[_type] >= _count:
                self.stor[_type] -= _count
                return {_type.__name__: _count}
            else:
                print(f"Недостаточное количество. В наличии {self.stor[_type]}")
                out = self.stor[_type]
                self.stor[_type] -= self.stor[_type]
                return {_type.__name__: out}
        else:
            print(f"Нет и никогда небыло в наличии {_type.__name__} на складе {self.me}")
            return False

    def move_to_other_stor(self, _type, _count, local):
        m = self.move_out_store(_type, _count)
        if m:
            return local.move_in_store(_type, m[_type.__name__])
        else:
            print("Нет объектов для перемещения")
            return False

    @staticmethod
    def check_type(_type):
        if _type in Equipment.__subclasses__():
            return True
        else:
            print("Тип с таким именем не существует")
            return False


class Err(Exception):
    def __init__(self, _type):
        print(f"Не валидный объект, хранится только {_type}")


class Equipment:

    @classmethod
    def types(cls):
        return [c.__name__ for c in cls.__subclasses__()]


class Printer(Equipment):
    cost = 100


class Scanner(Equipment):
    cost = 150


class Xerox(Equipment):
    cost = 80


store = StoreEquipment("store")
management = StoreEquipment("management")
accounting = StoreEquipment("accounting")
legal_department = StoreEquipment("legal_department")

stores = {"store": store,
          "management": management,
          "accounting": accounting,
          "legal_department": legal_department}

types = {"Printer": Printer,
         "Scanner": Scanner,
         "Xerox": Xerox}

while True:
    print(f"Список типов оргтехники: {', '.join(Equipment.types())}")
    user_t = input("Введите тип: ")
    if user_t == "exit":
        break

    if user_t in Equipment.types():
        user_t = types[user_t]
        user_c = input("Введите количество: ")
        try:
            user_c = int(user_c)
        except ValueError:
            print("Некорректное значение")
            continue
        print(f"Варианты действий:\n"
              f"1 - добавить на склад\n"
              f"2 - забрать со склада\n"
              f"3 - переместить")
        action = input("Введите номер варианта действия: ")
        if action in ["1", "2", "3"]:
            action = int(action)
            stores_string = ', '.join(stores.keys())
            if action == 1:
                user_s = input(f"выбери склад\n"
                               f"{stores_string}:\n")
                if user_s not in stores.keys():
                    print("")
                    continue
                user_stor = stores[user_s]
                user_stor.move_in_store(user_t, user_c)
            elif action == 2:
                user_s = input(f"выбери склад\n"
                               f"{stores_string}:\n")
                if user_s not in stores.keys():
                    print("Склад не найден")
                    continue
                user_stor = stores[user_s]
                user_stor.move_out_store(user_t, user_c)
            elif action == 3:
                r_source = input(f"Выберите локацию, из которой необходимо перенести, из списка\n"
                                 f"{stores_string}: ")
                r_target = input(f"Выберите локацию, в которую необходимо перенести, из списка\n"
                                 f"{stores_string}: ")
                if r_source not in stores.keys() or r_target not in stores.keys():
                    print("Склад не найден")
                    continue
                source = stores[r_source]
                target = stores[r_target]
                if source.move_to_other_stor(user_t, user_c, target):
                    print(f"перемещение успешно {target.state[user_t.__name__]} {user_t.__name__}\n"
                          f"со склада {r_source} на склад {r_target}")

    else:
        print(f"Список типов оргтехники: {', '.join(Equipment.types())}\n"
              f"Выберите значение из списка")


print("Итоговая информация\n"
      "-------------------")
for el in stores:
    if stores[el].inventory:
        print(f"На складе {el}")
        for eq, c in stores[el].state.items():
            print(f"{eq.__name__} - {c}")
        print(f"Оборудование общей стоимостью {stores[el].total_cost}")
    print("-------------------")