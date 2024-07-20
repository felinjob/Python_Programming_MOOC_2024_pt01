# Write your solution here

while True: 
    name = input("Please tell me your name: ")

    if name == "Jerry":
        print("Next please!")
        break

    portion = int(input("How many portions of soup? ")) * 5.90


    print("The total cost is", portion)
    print("Next please!")
    break
