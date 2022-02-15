use_values = input("Enter data: ")
l_values = use_values.split()
new_value = []

while l_values:
    if len(l_values) > 1:
        first_value = l_values.pop(1)
        second_value = l_values.pop(0)
        new_value.append(first_value)
        new_value.append(second_value)
    elif len(l_values) == 1:
        new_value.extend(l_values)
        break
print(new_value)
