# write your solution here
def creating_matrix():
    with open("matrix.txt") as new_file:
        list_numbers = []
        for line in new_file:    
            line = line.replace("\n", "")
            parts = line.split(",")
            list_numbers += [parts]
        return list_numbers
    
def int_matrix():
    lista = creating_matrix()
    for row in range(len(lista)):
        for number in range(len(lista[row])):
            lista[row][number] = int(lista[row][number])
    return lista
    
def matrix_sum():
    lista = int_matrix()
    soma = 0
    for row in lista:
        for number in row:
            soma += number
    return soma
    
def matrix_max():
    lista = int_matrix()
    max_val = 0
    for row in lista:
        for number in row:
            if number > max_val:
                max_val = number
    return max_val
    
def row_sums():
    lista = int_matrix()
    rows = []
    for row in lista:
        soma = 0
        for number in row:
            soma += number 
        rows += [soma]
    return rows
    
    
if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())