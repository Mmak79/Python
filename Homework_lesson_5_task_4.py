d = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_4.txt", "r") as num:
    content = num.readlines()
l_num = []
for el in content:
    data = el.split(" - ")
    numeral = data[0]
    num = int(data[1].strip("\n"))
    n_d = f"{d.get(numeral)} - {num}\n"
    l_num.append(n_d)
print("".join(l_num))
with open("text_4_1.txt", "w") as t_num:
    t_num.write("".join(l_num))
