def even_numbers(numbers: list):
    new_list = []
    for i in numbers:
        if i % 2 == 0:
            new_list.append(i)
    return new_list
 
if __name__ == "__main__":
    even_numbers()