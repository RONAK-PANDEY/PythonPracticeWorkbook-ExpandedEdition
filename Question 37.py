numbers = list(map(int, input().split()))
found = False

for num in numbers:
    if num < 0:
        print(num)
        found = True
        break  
if not found:
    print("Nonegative")
