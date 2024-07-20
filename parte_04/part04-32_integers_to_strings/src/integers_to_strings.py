# Write your solution here
def formatted(my_list: list):
    new_list =[]
    for itens in my_list:
        new_list.append(f"{itens:.2f}")
    return new_list
 
if __name__ == "__main__":
    formatted()