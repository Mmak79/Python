seasons_dict = {"winter": [12, 1, 2],
                "spring": [3, 4, 5],
                "summer": [6, 7, 8],
                "autumn": [9, 10, 11]}
u_m = int(input("Enter month number: "))
while 12 < u_m or u_m <= 0:
    u_m = input("Enter month number from 1 to 12: ")

for k, v in seasons_dict.items():
    if u_m in v:
        print("it is-", k)
