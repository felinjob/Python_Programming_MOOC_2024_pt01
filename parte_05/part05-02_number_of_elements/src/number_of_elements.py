# Write your solution here
def count_matching_elements(matrix: list, element: int):
    count = 0
    for row in matrix:
        for item in row:
            if item == element:
                count += 1
    return count
    
if __name__ == "__main__":  
    count_matching_elements()