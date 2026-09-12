command = input()

is_paused = False

if command == "START":
    print("Running")
elif command == "STOP":
    print("Stopped")
elif command == "PAUSE":
    pass  
    is_paused = True  
    
if is_paused:
    print("Feature Pending")
