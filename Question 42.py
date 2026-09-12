numbers = list(map(int, input().split()))


positive_sum = 0


for num in numbers:
    if num <= 0:
        continue  
    positive_sum += num

print(positive_sum)
