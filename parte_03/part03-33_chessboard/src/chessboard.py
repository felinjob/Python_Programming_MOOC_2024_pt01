def chessboard(value):
    string = "10"
    index = 0
    while index < value:
        word = string * value
        print(word[index:index+value])
        index += 1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
