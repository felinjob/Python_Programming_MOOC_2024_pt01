# Write your solution here
number = int(input("Please type in a number: "))
ref = 1
while ref <= number:
    i = 1
    while i <= number:
        print(f"{ref} x {i} = {ref*i}")
        i += 1
    ref += 1