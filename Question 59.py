a, b = map(int, input().split())

num1 = a
num2 = b


while b != 0:
    a, b = b, a % b

gcd_value = a

lcm_value = (num1 * num2) // gcd_value

print(f"gcd: {gcd_value}")
print(f"lcm: {lcm_value}")
