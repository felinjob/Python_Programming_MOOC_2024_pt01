# Write your solution here
times = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
spend = float(input("How much money do ou spend on groceries in a week? "))

weekly = price * times + spend
daily = weekly / 7

print("Average food expenditure:")
print("Daily:", daily, "euros")
print("Weekly:", weekly, "euros")