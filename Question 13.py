marks = int(input())

match marks:
    case m if m >= 90:
        print("A")
    case m if 80 <= m <= 89:
        print("B")
    case m if 70 <= m <= 79:
        print("C")
    case m if 60 <= m <= 69:
        print("D")
    case _:
        print("F")
