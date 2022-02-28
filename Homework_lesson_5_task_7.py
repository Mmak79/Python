import json
average_profit = []
s_f = {}
a_p = {}
final_list = []
with open("text_7.txt", "r") as firm:
    while True:
        content = firm.readline()
        if not content:
            break
        st = content.split(" ")
        name = st[0]
        t_o = st[1]
        revenue = int(st[2])
        costs = int(st[3])
        profit = revenue - costs
        if profit > 0:
            average_profit.append(profit)
        s_f[name] = profit

average_profit = sum(average_profit)
a_p["average_profit"] = average_profit
final_list.append(s_f)
final_list.append(a_p)

print(final_list)

with open("my_file.json", "w", encoding="utf-8") as f_j:
    json.dump(final_list, f_j, ensure_ascii=False)
