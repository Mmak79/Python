def two_out_of_three(var):
    var.remove(min(var))

    return sum(var)


var_1 = int(input("Enter number: "))
var_2 = int(input("Enter number: "))
var_3 = int(input("Enter number: "))


min_var = two_out_of_three([var_1, var_2, var_3])
print(min_var)
