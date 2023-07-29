age = int(input("Enter your age: "))

years_remaining = 90-age
days_remaining = years_remaining*365
weeks_remaining = years_remaining*52
month_remaining = years_remaining*12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, {month_remaining} months and {years_remaining} years")