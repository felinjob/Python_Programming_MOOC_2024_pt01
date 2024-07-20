# Write your solution here
from fractions import Fraction
    
    
def fractionate(amount: int):
    lista = []
    for value in range(amount):
        lista.append(Fraction(1, amount))
    return lista
    
if __name__ == "__main__":
    fractionate()