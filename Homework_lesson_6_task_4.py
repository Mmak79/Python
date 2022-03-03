class Car:
    def __init__(self, sp, cl, nm, i_p=False):
        self.speed = int(sp)
        self.color = cl
        self.name = nm
        self.is_police = bool(i_p)

    def on_go(self):
        print(f"go a car {self.color} {self.name}")

    def on_stop(self):
        self.speed = 0
        print(f"stop a car {self.color} {self.name}")

    def on_turn(self, direction):
        print(f"car {self.color} {self.name} turn {direction}")

    def show_speed(self):
        if self.is_police:
            print("Unlimited speed for police car")
        else:
            print(f"speed a car now {self.speed}")


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Attention! Over speed")
        else:
            print(f"speed a car now {self.speed}")


class SportCar(Car):

    def show_speed(self):
        if self.is_police:
            print("unlimited speed")
        elif self.speed > 180:
            print("Attention! Over speed")
        else:
            print("All right")


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Attention! Over speed")
        else:
            print(f"speed a car now {self.speed}")


class PoliceCar(Car):
    is_police = True


car = Car(75, "black", "Mazda")
car.on_go()
car.on_turn("left")
car.show_speed()
car.on_stop()
car.show_speed()
print()
t_c = TownCar(65, "red", "Cooper")
t_c.on_go()
t_c.on_turn("right")
t_c.show_speed()
t_c.on_stop()
t_c.show_speed()
print()
s_c = SportCar(180, "yellow", "Maserati")
s_c.on_go()
s_c.on_turn("right")
s_c.show_speed()
s_c.on_stop()
s_c.show_speed()
print()
w_c = WorkCar(45, "blue", "Зил")
w_c.on_go()
w_c.on_turn("left")
w_c.show_speed()
w_c.on_stop()
w_c.show_speed()
print()
p_c = PoliceCar(190, "White", "Opel", True)
p_c.on_go()
p_c.on_turn("left")
p_c.show_speed()
p_c.on_stop()
p_c.show_speed()
