# Write your solution here

first = int(input("Please type in the first number: "))
second = int(input("Please type in the another number: "))

value = max(first, second)

if first == second:
    print("The numbers are equal!")
else:
    print(f"The greater number was: {value}")