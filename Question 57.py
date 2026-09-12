n = int(input())

if n <= 3:
    print("NotEligible")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Eligible")
            break 
    else:
        print("NotEligible")
