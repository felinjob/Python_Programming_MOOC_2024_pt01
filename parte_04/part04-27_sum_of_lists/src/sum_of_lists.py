def list_sum(num: list, num2: list):
    index = 0
    new_list = []
    while index < len(num):
        new_list.append(num[index] + num2[index])
        index += 1
    return new_list
 
if __name__ == "__main__":
    list_sum()