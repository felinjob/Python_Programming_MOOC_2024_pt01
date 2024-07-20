# Write your solution here
def shortest(my_list: list):
    length = ""
    for item in my_list:
        if len(item) > len(length):
            length = item
    for item in my_list:
        if len(item) < len(length):
            length = item
    return length
 
 
if __name__ == "__main__":
    shortest()