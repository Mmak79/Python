from itertools import cycle

a = [3, 4, 5, 6, 7, 8, 9, 12]

d = 0
for el in cycle(a):
    if d > 40:
        break
    print(el)
    d += 1
