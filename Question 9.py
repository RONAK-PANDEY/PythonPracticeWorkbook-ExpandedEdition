u = int(input())


if u <= 100:
    bill = u * 2
elif u <= 200:
    bill = (100 * 2) + ((u - 100) * 3)
else:
    bill = (100 * 2) + (100 * 3) + ((u - 200) * 5)


print(f"bill: {bill}")
