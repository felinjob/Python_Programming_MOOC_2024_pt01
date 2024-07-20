# Write your solution here
phoneBook = {}
    
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    
    if command == 1:
        name = input("name: ")
        if name in phoneBook:
            print(phoneBook[name])
        else:
            print("no number")
        continue
    elif command == 2:
        name = input("name: ")
        number = input("number: ")
        print("ok!")
        phoneBook[name] = number
        continue
    elif command == 3:
        print("quitting...")
        break