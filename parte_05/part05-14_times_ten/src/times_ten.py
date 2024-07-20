# Write your solution here
def times_ten(start_index: int, end_index: int):
    new_dic = {}
    for item in range(start_index, end_index + 1):
        new_dic[item] = item * 10
    return new_dic
    
if __name__ == "__main__":
    times_ten()