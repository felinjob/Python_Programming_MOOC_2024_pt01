# Write your solution here
value = int(input("Value of gift: "))

if value > 5000:
    if 5000 < value < 25000:
        value = 100 + (value - 5000) * 0.08
    elif 25000 < value < 55000:
        value = 1700 + (value - 25000) * 0.10
    elif 55000 < value < 200000:
        value = 4700 + (value - 55000) * 0.12
    elif 200000 < value < 1000000:
        value = 22100 + (value - 200000) * 0.15
    elif value > 1000000:
        value = 142100 + (value - 1000000) * 0.17
    print(f"Amount of tax: {float(value)} euros")
else:
    print("No taxes!") 