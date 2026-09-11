pin = int(input("Enter you pin: "))


if pin == 4321:
    print("Access Granted")
else:
    while pin != 4321:
        x = int(input("(2nd attempt) Enter your pin: "))
        if x == 4321:
            print("Access Granted")
            break  
        elif x != 4321:
            y = int(input("(3rd attempt) Enter your pin: "))
            if y != 4321:
                print("Card block")
                break  
            elif y == 4321:
                print("Access Granted")
                break  
