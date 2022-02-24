i = [4, 7, 7, 8, 99, 99, 99, 3, 2, 3, 4, 678, 32, 2, 45, 66]

new_el = [i[el] for el in range(len(i)) if i[el] > i[el-1]]

print(new_el)
