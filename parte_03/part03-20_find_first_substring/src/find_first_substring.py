# Write your solution here
word = input("Please type in a word: ")
substring = input("Please type in a character: ")
index = word.find(substring)

if index != -1 and len(word) >= index + 3:
    print(word[index:index+3])