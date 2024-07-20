# Write your solution here
myList = []
while True:
    word = input("Word:")
    if word in myList:
        break
    myList.append(word)
print(f"You typed in {len(myList)} different words")