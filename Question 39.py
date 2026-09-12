numbers = list(map(int, input().split()))

total_sum = 0

for i in numbers:
    if i == 0:
        break
    total_sum += i
    
print(f"sum:{total_sum}")
    
