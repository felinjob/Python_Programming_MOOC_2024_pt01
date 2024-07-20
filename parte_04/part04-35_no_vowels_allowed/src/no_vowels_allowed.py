# Write your solution here
def no_vowels(string: str):
    no_vow = ""
    vowels = "aeiou"
    for letter in string:
        if letter not in vowels:
            no_vow += letter
    return no_vow
 
if __name__ == "__main__":
    no_vowels()