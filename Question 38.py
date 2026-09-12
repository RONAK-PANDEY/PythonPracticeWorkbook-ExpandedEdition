n = int(input())
m = int(input())

found = False
for i in range(n, m + 1):
    if i % 4 == 0 and i % 6 == 0:
        found = True
        print(i)
        break

if not found:
    print("Notfound")
