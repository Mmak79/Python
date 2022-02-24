my_list = list(range(20, 241))

new = [i for i in my_list if i % 20 == 0 or i % 21 == 0]

print(new)
