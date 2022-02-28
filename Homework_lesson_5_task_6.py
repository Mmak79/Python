def my_func(s):
    sp = s.strip(' ').split(" ")
    l_num = []
    for k in sp:
        n = k.split("(")
        try:
            num = int(n[0])
        except Exception:
            num = 0
        l_num.append(num)
    return sum(l_num)


s_s = {}
with open("text_6.txt", "r") as syllabus:
    content = syllabus.readlines()

for i in content:
    el = i.split(":")
    name = el[0]
    h = my_func(el[1])
    s_s[name] = h
print(s_s)
