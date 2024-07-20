# Write your solution here
while True:
    number = int(input("Please type in a number: "))
    i = 1
    count = 1
    if number > 0:
        while count <= number:
            i *= count
            count += 1
        print(f"The factorial of the number {number} is {i}")
    else:
        print("Thanks and bye!")
        break