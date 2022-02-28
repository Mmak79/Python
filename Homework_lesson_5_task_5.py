num = [str(el) for el in range(2, 35)]
with open("text_5.txt", "w") as number:
    number.write(f"{' '.join(num)}\n")
with open("text_5.txt", "r") as number:
    content = number.readlines()
    el = content[0].split(" ")
n_num = [int(i) for i in el]
print(f"Сумма чисел: {sum(n_num)}")
