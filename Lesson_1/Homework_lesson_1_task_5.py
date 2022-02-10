revenue = int(input("Enter revenue: "))
costs = int(input("Enter costs: "))

financial_results = int(revenue) - int(costs)
if financial_results > 0:
    print("you financial results positive and = ", financial_results)
if financial_results < 0:
    print("you financial results negative and = ", financial_results)
if financial_results == 0:
    print("you financial results = ", financial_results)


