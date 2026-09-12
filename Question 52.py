numbers = list(map(int, input().split()))
target = int(input())

for num in numbers:
    if num == target:
        print("Found")
        break  
else:
    print("NotFound")
