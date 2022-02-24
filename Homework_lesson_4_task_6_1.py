from itertools import count

r = []

for i in count(5):
    r.append(i)
    if i > 20:
        break

print(r)

