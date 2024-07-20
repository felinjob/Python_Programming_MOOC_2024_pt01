# Write your solution here
def find_movies(database: list, search_term: str):
    search = str(search_term).lower()
    datareturn = []
    for itens in database:
        value =  str(itens["name"]).lower()
        if search in value:
            datareturn.append(itens)
    return datareturn
    
if __name__ == "__main__":
    find_movies()