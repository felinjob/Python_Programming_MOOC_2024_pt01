# Write your solution here
def all_the_longest(my_list: list):
    length = ""
    new_list =[]
    for item in my_list:
        if len(item) >= len(length):
            length = item
    for item in my_list:
        if len(item) == len(length):
            new_list.append(item)
    return new_list
 
if __name__ == "__main__":
    print(all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))
