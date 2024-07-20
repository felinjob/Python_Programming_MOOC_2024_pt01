# Write your solution here
def length_of_longest(my_list: list):
    length = ""
    for item in my_list:
        if len(item) > len(length):
            length = item
    return len(length)
 
 
if __name__ == "__main__":
    length_of_longest()