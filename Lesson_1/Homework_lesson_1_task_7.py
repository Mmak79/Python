from itertools import count

a = int(input("Enter current distance (km): "))
b = int(input("Enter target distance (km): "))
c = 0.1
day = 1

while a < b:
    day = day + 1
    delta = a * c
    a = a + delta

print(day)







