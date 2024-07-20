# Write your solution here
limit = int(input("Limit: "))
count = 1
add = 1
value = ""
while add < limit:
    value += f"{count} + "
    count += 1
    add += count    
print(f"The consecutive sum: {value}{count} = {add}")