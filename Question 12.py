a = int(input())
b = int(input())
op = input().strip()

match op:
    case '+':
        print(a + b)
    case '-':
        print(a - b)
    case '*':
        print(a * b)
    case '/':
        print(a / b)
    case _:
        print("Invalid operator")
