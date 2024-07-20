# Write your solution here
def everything_reversed(my_list: list):
    new_list = []
    for i in my_list:
        object = str(i)
        revert = object[::-1]
        new_list.insert(0,revert)
    return new_list
 
if __name__ == "__main__":
    everything_reversed()