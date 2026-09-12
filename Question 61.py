salary = float(input())
gender = input().strip()

if gender == 'M':
    bonus_percent = 5.0
elif gender == 'F':
    bonus_percent = 10.0
else:
    bonus_percent = 0.0

if salary < 10000:
    bonus_percent += 2.0

bonus_amount = salary * (bonus_percent / 100.0)
total_salary = salary + bonus_amount

print(f"{bonus_amount:.2f}")
print(f"{total_salary:.2f}")
