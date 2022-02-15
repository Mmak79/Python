month_list = ["winter", "spring", "summer", "autumn"]
u_m = input("Enter month number: ")

if u_m in [12, 1, 2]:
    print(month_list[0])
if u_m in [3, 4, 5]:
    print(month_list[1])
if u_m in [6, 7, 8]:
    print(month_list[2])
if u_m in [9, 10, 11]:
    print(month_list[3])
