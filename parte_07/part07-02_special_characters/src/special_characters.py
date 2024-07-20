# Write your solution here
import string
    
def separate_characters(my_string: str):
    letters = ""
    punctuation = ""
    others = ""
    for letter in my_string:
        if letter in string.ascii_letters:
            letters += letter
        elif letter in string.punctuation:
            punctuation += letter
        else:
            others += letter
    
    return letters, punctuation, others
    
    
if __name__ == "__main__":
    separate_characters()