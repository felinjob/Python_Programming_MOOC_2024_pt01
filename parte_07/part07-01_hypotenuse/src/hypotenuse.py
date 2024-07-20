# Write your solution here
import math
    
def hypotenuse(leg1: float, leg2: float):
    hypo = (leg1 ** 2) + (leg2 ** 2)
    return math.sqrt(hypo)
    
if __name__ == "__main__":
    hypotenuse()