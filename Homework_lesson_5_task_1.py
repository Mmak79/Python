st = input("print: ")
try:
    with open("text.txt", "w", encoding="utf-8") as use:
        while st:
            use.write(f"{st}\n")
            st = input("print: ")
except Exception as e:
    print(f"какая-то ошибка\n{e}")
