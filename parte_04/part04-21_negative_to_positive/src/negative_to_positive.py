# Write your solution here
number = int(input("Please type n a positive integer: "))
negative = number * -1
for i in range(negative, number +1):
    if i == 0:
        continue
    print(i)