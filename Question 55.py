username = input()

for char in username:
    is_lower = 'a' <= char <= 'z'
    is_upper = 'A' <= char <= 'Z'
    is_digit = '0' <= char <= '9'
    
    if not (is_lower or is_upper or is_digit):
        print("Invalid")
        break
else:
    print("Valid")
