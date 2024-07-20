# Write your solution here
sent = input("Please type in a sentence: ")
index = 0
find = " "

while True:
    print(sent[index])
    while index < len(sent):
        word = sent[index]
        if find == word:
            print(sent[index + 1])
        index += 1
    break