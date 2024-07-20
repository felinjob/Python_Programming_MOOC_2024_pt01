# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    column_list = []
    column_check = []
    index = 0
    while index < 3:
        row_list = []
        for row in sudoku[row_no + index]:
            row_list.append(row)  
        column_list.append(row_list[column_no:column_no + 3])  
        index += 1
    for lists in column_list:
        for square in lists:
            if square > 0 and square in column_check:
                return False
            column_check.append(square)
    return True      
    
    
    
    
if __name__ == "__main__":
    block_correct()