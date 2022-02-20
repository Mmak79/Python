def my_func_2(x, y):
    degree_of_x = 1 / (my_func_3(x, y))
    return degree_of_x


a = int(input("Enter number: "))
b = int(input("Enter a negative number: "))


def my_func_3(z, g):
    res = z
    c = abs(g)
    for el in range(1, c):
        res = res * z
    return res


print(my_func_2(a, b))
