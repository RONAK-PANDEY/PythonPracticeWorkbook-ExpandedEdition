n = int(input())
current = 2
total_sum = 0


while current <= n:
    total_sum += current
    current += 2  
print(f"sum: {total_sum}")
