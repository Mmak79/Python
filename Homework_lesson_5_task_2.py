n = 1
with open("Homework_lesson_5_task_2.txt", "r") as file:
    content = file.readlines()
print(f"Количество строк в файле: {len(content)}")
for el in content:
    st = el.split(" ")
    print(f"Количество слов в строке {n}: {len(st)}")
    n += 1
