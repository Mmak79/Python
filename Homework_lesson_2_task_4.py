a = input("Enter names:  ").split()

for ind, el in enumerate(a, 1):
    print(ind, ")", el[:10])
