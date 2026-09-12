a = int(input())
b = int(input())

filtered_sum = 0

for i in range(a, b + 1):
    if i % 4 == 0 or i % 6 == 0:
        continue  
    filtered_sum += i
print(f"sum: {filtered_sum}")
