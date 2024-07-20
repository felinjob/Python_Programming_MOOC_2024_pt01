# Write your solution here
def distinct_numbers(numbers: list):
    new_list = []
    sort = sorted(numbers)
    for iten in sort:
        if iten not in new_list:
            new_list.append(iten)
    return new_list
 
if __name__ == "__main__":
    distinct_numbers()