n = int(input("Enter number"))
list1 = []
for i in range(1, n+1):
    x = i ** 2
    list1.append(x)
    
print(sum(list1))
