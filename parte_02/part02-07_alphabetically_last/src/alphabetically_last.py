# Write your solution here
w1 = input("Please type in the 1st word: ")
w2 = input("Please type in the 2nd word: ")

word = max(w1, w2)

if w1 == w2:
    print("You gave the same word twice.")
else:
    print(f"{word} comes alphabetically last")