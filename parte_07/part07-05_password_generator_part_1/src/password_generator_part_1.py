# Write your solution here
import string, random
    
def generate_password(length: int):
    tese = ""
    for letter in random.sample(str(string.ascii_lowercase), length):
        tese += letter
    return tese
    
    
if __name__ == "__main__":
    generate_password()