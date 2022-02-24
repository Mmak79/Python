from functools import reduce


def my_fac(y):
    x = range(1, y + 1)
    for a in x:
        yield reduce(my_func, range(1, a + 1))


def my_func(prev_el, el):
    return prev_el * el


for n in my_fac(13):
    print(n)
