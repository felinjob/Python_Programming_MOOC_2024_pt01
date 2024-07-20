# Write your solution here
myList = []
while True:
    new = int(input("New item: "))
    if new == 0:
        break
    myList.append(new)
    print(f"The list now: {myList}")
    print(f"The list in order: {sorted(myList)}")
print("Bye!")