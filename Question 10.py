admin = str(input("Enter the admin: ").strip())
pin = int(input("Enter the pin: ").strip())

if admin == "admin":
    if pin == 2468:
        print("Access Granted")
        
else:
    print("Wrong pin or admin")
