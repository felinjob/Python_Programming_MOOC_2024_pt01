# write your solution here
word_dict = {}
with open("wordlist.txt") as new_file:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        word_dict[letter] = []
    for files in new_file:            
        word = files.strip()
        word_dict[word[0]].append(word)
    
string = input("Write text: ")
    
split_string = string.split(" ")
    
    
return_str = ""
for word in split_string:    
    check = word.lower()
    if check not in word_dict[check[0]]:
        return_str += "*" + word + "*" + " "
        continue
    return_str += word + " "
    
print(return_str)