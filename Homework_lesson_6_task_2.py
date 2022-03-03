class Road:
    def __init__(self, _l, _w):
        self._length = _l
        self._width = _w

    def all_road(self, m, sm):
        res = self._length * self._width * m
        all_res = res * sm
        return round(all_res / 1000)


road = Road(5000, 20)
print(road.all_road(25, 5))
