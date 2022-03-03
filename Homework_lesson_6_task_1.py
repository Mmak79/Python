import time


class TrafficLight:
    __light = "color"

    def running(self, r_iter=10):
        i_i = 0
        while i_i < r_iter:
            print(self.__light, 'red')
            time.sleep(7)
            print(self.__light, 'yellow')
            time.sleep(2)
            print(self.__light, 'green')
            time.sleep(5)
            print(self.__light, 'yellow')
            time.sleep(2)
            i_i += 1


run = TrafficLight()
run.running()
