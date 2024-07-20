def palindromes(word: str):
    rev_string = ""
    for i in word[::-1]:
        rev_string += i
    return rev_string == word
 
 
def palindromes_2():
    while True:
        string = input("Please type in a palindrome: ")
        rev_string = ""
        for i in string[::-1]:
            rev_string += i
        
        if rev_string == string:
            print(string, "is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")
 
palindromes_2()
