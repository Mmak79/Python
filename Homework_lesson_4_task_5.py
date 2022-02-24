from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


my_list = list(range(100, 1002, 2))

work = reduce(my_func, my_list)
print(work)
