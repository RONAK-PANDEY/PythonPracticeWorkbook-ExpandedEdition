code = input()

for char in code:
    if not ('0' <= char <= '9'):
        print("Invalid")
        break  
else:
    print("Valid")
