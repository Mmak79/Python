

temp = int(input("enter temperature today: "))
month = str(input("enter month: "))
day = int(input("enter day of the month: "))
if temp <= -10:
    print(f"{day} {month} very cold")
elif -10 < temp <= 5:
    print(f"{day} {month} pretty cold")
elif 5 < temp <= 20:
    print(f"{day} {month} heat")
else:
    print(f"{day} {month} hot")
