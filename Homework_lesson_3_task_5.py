n = 0
ex = False
while True:
    my_list = input("Enter a string of numbers separated by spaces: ").split()
    for a in my_list:
        try:
            n = n + int(a)
        except ValueError:
            if a == "e" or a == "exit":
                ex = True
                break
        except Exception as Error:
            print(Error)
    print(f"sum = {n} (for exit, enter 'e' or 'exit')")
    if ex:
        break
