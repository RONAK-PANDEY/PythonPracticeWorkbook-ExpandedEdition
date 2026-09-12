n, m = map(int, input().split())

found = False

for i in range(n, m):
    if i % 5 == 0:
        print(i)
        found = True
        break  
if not found:
    print("Notfound")
