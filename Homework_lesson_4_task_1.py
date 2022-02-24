from sys import argv


def my_func(v_1, v_2, v_3):
    res = v_1 * v_2 + v_3
    return res


name, h, s, b = argv

print(my_func(int(h), int(s), int(b)))
