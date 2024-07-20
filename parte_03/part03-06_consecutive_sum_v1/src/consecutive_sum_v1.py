# Write your solution here
limit = int(input("Limit: "))
count = 0
add = 0
while add < limit:
    count += 1
    add += count
print(add)