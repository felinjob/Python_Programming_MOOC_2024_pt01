# Write your solution here
import random
    
def lottery_numbers(amount: int, lower:int, upper: int):
    return sorted(random.sample(list(range(lower, upper)), amount))
    
    
if __name__ == "__main__":
    lottery_numbers()