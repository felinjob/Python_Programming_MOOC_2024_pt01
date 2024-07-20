# Write your solution here
def no_shouting(my_list: list):
    pruned = []
    for i in my_list:
        if not i.isupper():
            pruned.append(i)
    return pruned
 
if __name__ == "__main__":
    no_shouting()