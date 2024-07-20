# Write your solution here
words = ""
repeat = ""
while True: 
    word = input("Please type in a word: ")
    if repeat == word:
        break
    if word == "end":
        break
    words += word + " "
    repeat = word
print(words)