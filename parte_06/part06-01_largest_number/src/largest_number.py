def largest():
    with open("numbers.txt") as numb_list:
        print(numb_list)
        list_numbers = []
    
        for line in numb_list:
            line = int(line.replace("\n", ""))
            list_numbers += [line]
        
    return max(list_numbers)
    
if __name__ == "__main__":
    largest()
