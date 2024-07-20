# Write your solution here
def anagrams(first, second):
    if sorted(first) == sorted(second):
        return True
    else:
        return False
 
if __name__ == "__main__":
    anagrams()   