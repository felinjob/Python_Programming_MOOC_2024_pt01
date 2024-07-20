# Write your solution here
number = int(input("Please type in a number: "))

numba = 0
numbb = 0

while numba <= number or numbb <= number:
    numba += 2
    numbb = numba - 1
    if numba <= number:
        print(numba)
    if numbb <= number:
        print(numbb)
    else:
        break