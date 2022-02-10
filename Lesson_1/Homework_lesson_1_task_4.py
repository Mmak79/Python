x = int(input("Enter integer: "))
current_max = 0

while x > 0:
    current = x % 10
    x = x // 10
    if current > current_max:
        current_max = current
print(current_max)


