# Write your solution here
itens = int(input("How many itens: "))
myList = []
count = 1
while 0 < itens:
    
    iten = int(input(f"Item {count}: "))
    myList.append(iten)
    count += 1
    itens -= 1
 
print(myList)