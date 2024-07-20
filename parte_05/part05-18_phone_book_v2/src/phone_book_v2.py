# Write your solution here
def addPerson(phoneBook):
    name = input("name: ")
    number = input("number: ")
    if name not in phoneBook:
        phoneBook[name] = []
    phoneBook[name].append(number)
    print("ok!")
    
def searchPerson(phoneBook):
    name = input("name: ")
    if name in phoneBook:
        for number in phoneBook[name]:
            print(number)
    else:
        print("no number")
    
def phone():
    phoneBook = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 3:
            print("quitting...")
            break
        elif command == 1:
            searchPerson(phoneBook)
            continue
        elif command == 2:
            addPerson(phoneBook)
            continue
    
phone()