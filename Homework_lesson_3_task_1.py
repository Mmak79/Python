def my_f(dividend, divider):
    try:
        result = dividend / divider
    except ZeroDivisionError as e:
        print(e)
        return "Error"
    return result


d_1 = int(input("Enter dividend: "))
d_2 = int(input("Enter divider: "))
print(my_f(d_1, d_2))
