# Write your solution here
myList = []
count = 1
while True:
    print(f"The list is now {myList}")
    operation = input("a(d)d, (r)emove or e(x)it: ")
    if operation == "d":
        myList.append(count)
    elif operation == "r":
        myList.pop(-1)
        count -= 1
        continue
    elif operation == "x":
        print("Bye!")
        break
    count += 1