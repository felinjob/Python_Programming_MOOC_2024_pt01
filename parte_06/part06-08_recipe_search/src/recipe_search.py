# Write your solution here
def create_list(filename: str):
    recipes = {}
    with open(filename) as new_file:
        for lines in new_file:
            if lines == "\n":
                continue
            if lines[0].isupper():
                name = lines.strip()
                recipes[name] = []
                continue
            recipes[name].append(lines.strip())
    return recipes
    
def search_by_name(filename: str, word: str):
    recipes = create_list(filename)
    contain = []
    for recipe in recipes:
        if word in recipe.lower():
            contain.append(recipe)
    return contain
def search_by_time(filename: str, prep_time: int):
    recipes = create_list(filename)
    contain = []
    for recipe in recipes:
        value = int(recipes[recipe][0])
        if value <= prep_time:
            contain.append(f"{recipe}, preparation time {recipes[recipe][0]} min")
    return contain
def search_by_ingredient(filename: str, ingredient: str):
    recipes = create_list(filename)
    contain = []
    for recipe in recipes:
        if ingredient in recipes[recipe]:
            contain.append(f"{recipe}, preparation time {recipes[recipe][0]} min")
    return contain
    
            
if __name__ == "__main__":
    print(search_by_name("recipes1.txt", "cake"))
    print(search_by_time("recipes1.txt", 20))
    print(search_by_ingredient("recipes1.txt", "eggs"))