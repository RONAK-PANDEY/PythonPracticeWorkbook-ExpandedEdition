# Read the positive integer n
n = int(input())

reversed_num = 0

# Extract and shift digits using arithmetic
while n > 0:
    remainder = n % 10          # Get the last digit
    reversed_num = (reversed_num * 10) + remainder  # Shift existing digits left and add new digit
    n = n // 10                 # Remove the last digit from n

# Print the final reversed integer
print(reversed_num)
