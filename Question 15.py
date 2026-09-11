shape = input().strip()

match shape:
    case "SQUARE":
        side = int(input())
        area = side * side
        print(f"area: {area}")
        
    case "RECTANGLE":
        length = int(input())
        breadth = int(input())
        area = length * breadth
        print(f"area: {area}")
        
    case "TRIANGLE":
        base = int(input())
        height = int(input())
        area = 0.5 * base * height
        print(f"area: {area:.1f}")
        
    case _:
        print("Invalid shape")
