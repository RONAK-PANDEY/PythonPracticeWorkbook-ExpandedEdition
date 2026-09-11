words = input().split()

count = 0

for w in words:
    print(f'{w}: {len(w)}')
    count += 1
    
print('total:',count)
