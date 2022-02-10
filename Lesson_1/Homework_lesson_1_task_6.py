revenue = int(input("Enter revenue: "))
costs = int(input("Enter costs: "))
if costs < revenue:
    profit = int(revenue) - int(costs)
    # print(int(profit))
    if profit > 0:
        profit_result = int((profit / revenue) * 100)
        print(profit_result)
        num_of_emp = int(input("Enter number of employees: "))
        profit_result_for_1 = profit / num_of_emp
        print("Your profit_result_for_1: ", profit_result_for_1)






# if financial_results > 0
#
#     print("you financial results positive and = ", financial_results)
# if financial_results < 0:
#     print("you financial results negative and = ", financial_results)
# if financial_results == 0:
#     print("you financial results = ", financial_results)
