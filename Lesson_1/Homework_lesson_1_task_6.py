revenue = int(input("Enter revenue: "))
costs = int(input("Enter costs: "))
if costs < revenue:
    profit = int(revenue) - int(costs)

    if profit > 0:
        profit_result = int((profit / revenue) * 100)
        print(profit_result)
        num_of_emp = int(input("Enter number of employees: "))
        profit_result_for_1 = profit / num_of_emp
        print("Your profit_result_for_1: ", profit_result_for_1)
