balance, withdrawal = map(int, input().split())

if withdrawal <= 0:
    print("Invalidamount")

elif withdrawal % 100 != 0:
    print("Amountmustbemultipleof100")

elif withdrawal > balance:
    print("Insufficientbalance")
    
else:
    new_balance = balance - withdrawal
    print(f"newbalance:{new_balance}")
