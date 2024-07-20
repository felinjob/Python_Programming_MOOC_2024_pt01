# Write your solution here
def splitString(string):
    newList = string.split(" ")
    return newList
 
def first_word(string):
    first = splitString(string)
    return first[0]
def second_word(string):
    second = splitString(string)
    return second[1]
def last_word(string):
    last = splitString(string)
    return last[-1]
if __name__ == "__main__":
    first_word()
    second_word()
    last_word()
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))