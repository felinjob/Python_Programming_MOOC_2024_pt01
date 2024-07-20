# Write your solution here
def spruce(number):    
    numero = number
    space = " "
    spruce =  "*"
    count = 1
 
    print("a spruce!")
 
    while numero > 0:
        numero -= 1
        print(space * numero + spruce * count)
        count += 2
 
    numero = number
    space = " "
    spruce =  "*"
    count = 1
 
    print(space * (numero - 1) + spruce * count)
    



# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)