# Write your solution here
hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day = input("Day of the week:")

if day == "Sunday":
    salary = hourly_wage * 2 * hours_worked
else:
    salary = hourly_wage * hours_worked

print(f"Daily wages: {salary} euros")