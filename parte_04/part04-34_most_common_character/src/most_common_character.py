# Write your solution here
def most_common_character(string: str):
    new_list = []
    for i in string:
        new_list.append(string.count(i))
 
    common = max(new_list)
    index = 0
 
    while index < len(string):
        if common == new_list[index]:
            break
        index += 1
    return string[index]
 
if __name__ == "__main__":
    most_common_character()