temp = int(input("Enter the temperature: ").strip())

print("Cold" if temp < 15 else "Pleasant" if 15 <= temp <= 25 else "Warm" if 26 <= temp <= 35 else "Hot")
