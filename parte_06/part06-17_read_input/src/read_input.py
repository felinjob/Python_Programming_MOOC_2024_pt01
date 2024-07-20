# Write your solution here
def read_input(prompt: str, num1: int, num2: int):
    while True:
        try:
            number = int(input(prompt))
            if num1 <= number <= num2:
                return number
        except ValueError:
            pass
        
        print(f"You must type in an integer between {num1} and {num2}")
    
if __name__ == "__main__":
    read_input()