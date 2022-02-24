my_list = [4, 7, 7, 8, 99, 99, 99, 3, 2, 3, 4, 678, 32, 2, 45, 66]

new_my_list = [i for i in my_list if my_list.count(i) == 1]

print(new_my_list)
