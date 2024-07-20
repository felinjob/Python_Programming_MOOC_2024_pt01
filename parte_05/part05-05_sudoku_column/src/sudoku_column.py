# Write your solution here
def column_correct(sudoku: list, column_no: int):
    column_list = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in column_list:
            return False
        column_list.append(row[column_no])
    return True
	 
	 
	 
	 
if __name__ == "__main__":
    column_correct()