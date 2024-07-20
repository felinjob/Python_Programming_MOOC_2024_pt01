# Write your solution here
def sudoku_grid_correct(sudoku: list):
    
    index = 0
    while index < len(sudoku):
        check = []
        column_list = []
        for row in sudoku[index]:
            if row > 0 and row in check:  
                return False          
            check.append(row)
        
        for row in sudoku:
            if row[index] > 0 and row[index] in column_list:
                return False
            column_list.append(row[index])
    
        index += 1
    
    index = 0
    
    while index <= 6:
        index2 = 0
        while index2 <= 6:
            numbers = []
            for row in range(index, index + 3):
                for column in range(index2, index2 + 3):
                    number = sudoku[row][column]
                    if number > 0 and number in numbers:
                        return False
                    numbers.append(number)
            index2 += 3
        index += 3
    return True
    
    
if __name__ == "__main__":
    sudoku_grid_correct