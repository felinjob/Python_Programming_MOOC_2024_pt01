# Write your solution here
while True:
        entry = int(input("1 - add an entry, 2 - read entries, 0 - quit "))
        
        if entry == 0:
            print("Function:", entry)
            print("Bye now!")
            break
        elif entry == 1:
            print("Function:", entry)
            with open("diary.txt", "a") as my_file:
                diary_e = input("Diary entry: ")
                my_file.write(f"{diary_e}\n")
                print("Diary saved")
        elif entry == 2:
            # print("Function:", entry)
            # print("entries ")
            with open("diary.txt") as my_file:
                content = ""
                for line in my_file:
                    if line == "Entries: ":
                        continue
                    content += line
                print(content)
                break