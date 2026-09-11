integers = [int(x) for x in input().split()]
total_sum = 0

for num in integers:
    total_sum += num 
    
print(f'sum: {total_sum}')
