# Copy here code of line function from previous exercise and use it in your solution
def line(integer: int, string: str) -> str:
    if not string:
        print("*" * integer)
    else:
        print(integer * string[0])
        
def shape(val_1: int, char_1: str, val_2: int, char_2: str):
# You can test your function by calling it within the following block
    for i in range(val_1):
        line(i+1, char_1)
    for i in range(val_2):
        line(val_1, char_2)

if __name__ == "__main__":
    shape(5, "x", 2, "o")