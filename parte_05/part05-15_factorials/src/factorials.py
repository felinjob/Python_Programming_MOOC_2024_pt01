def factorials(n: int):
    dictio = {}    
    for number in range(n, 0, -1):
        factorial = 1
        index = number
        while index > 0:
            factorial *= index
            index -= 1
        dictio[number] = factorial
    
    return dictio
    
if __name__ == "__main__":
    factorials()