# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
add = 0
positive = 0
negative = 0
while True:
    number = int(input("Number: "))

    if number == 0:
        break
    if number > 0:
        positive += 1
    else:
        negative += 1
    add += number 
    count += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {add}")
print(f"The mean of the numbers is {add / count}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")