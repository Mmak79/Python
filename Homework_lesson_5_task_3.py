with open("text_3.txt", "r") as stat:
    content = stat.readlines()
print("Количество сотрудников: ", len(content))
l_m = []
l_smb = []
for el in content:
    data = el.split(" ")
    sn = data[0]
    m = float(data[1].strip("\n"))
    l_m.append(m)
    if m < 20000:
        l_smb.append(sn)
print(f"Средняя величина дохода сотрудников: {sum(l_m) / len(l_m)}")
print(f"Сотрудники, чья з/п, меньше 20000 рублей: {', '.join(l_smb)}")
