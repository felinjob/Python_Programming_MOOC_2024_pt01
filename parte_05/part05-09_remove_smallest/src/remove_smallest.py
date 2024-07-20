def remove_smallest(numbers: list):
    remove = sorted(numbers)[1:]
    for number in numbers:
        if number not in remove:
            numbers.remove(number)
    
if __name__ == "__main__":
    remove_smallest()