# Write your solution here
def same_chars(string, num1, num2):
    if num1 >= len(string) or num2 >= len(string):
        return False
    elif string[num1] == string[num2]:
        return True
    elif string[num1] != string[num2]:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))