# Copy here code of line function from previous exercise
def line(integer: int, string: str) -> str:
    if not string:
        print("*" * integer)
    else:
        print(integer * string[0])
        
def box_of_hashes(height):
    # You should call function line here with proper parameters
    for i in range(height):      
        line(10, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
