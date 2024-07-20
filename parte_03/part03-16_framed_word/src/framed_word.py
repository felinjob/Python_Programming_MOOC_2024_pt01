# Write your solution here
string = input("Please type in a string: ")
symbol = "*" + " " * ((28 - int(len(string))) // 2) + string + " " * ((29 - int(len(string))) // 2) + "*"


print("*" * 30)
print(symbol)
print("*" * 30)