# Write your solution here
def sum_of_positives(number: list):
    soma = 0
    for i in number:
        if i > 0:
            soma += i
    return soma
 
 
if __name__ =="__main__":
    sum_of_positives()