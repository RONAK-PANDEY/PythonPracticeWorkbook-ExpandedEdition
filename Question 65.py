amount = float(input("Order amount: "))
zone = input("Zone: ").strip()

is_valid_zone = True
charge = 0.0


if zone == "LOCAL":
    charge = 30.00 if amount < 1000 else 0.00
elif zone == "CITY":
    charge = 60.00 if amount < 1000 else 0.00
elif zone == "OUTSIDE":
    charge = 120.00  
else:
    is_valid_zone = False


if is_valid_zone:
    print(f"charge: {charge:.2f}")
else:
    print("Invalid zone")
