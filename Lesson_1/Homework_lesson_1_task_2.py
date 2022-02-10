
total_sec = int(input("enter time in seconds (0 - 86400): "))
if 0 <= total_sec <= 86400:

    hours = total_sec // 3600

    total_sec = total_sec - hours * 3600
    minutes = total_sec // 60

    seconds = total_sec - minutes * 60
    if hours <= 9:
        hours = f"0{hours}"

    if minutes <= 9:
        minutes = f"0{minutes}"

    if seconds <= 9:
        seconds = f"0{seconds}"

    print(f"{hours}:{minutes}:{seconds}")
else:
    print("try again, though not necessary...")


