total_budget = list(map(int, input("Enter the total budget, food, and travel cost: ").split()))
total_spend = total_budget[1] + total_budget[2]
total_remaning_amount = total_budget[0] - total_spend



print("Remaining Amount:", abs(total_remaning_amount))
