# Write your solution here
def new_person(name:str, age: int):
    try:
        if len(name) > 0 and len(name) < 40 and " " in name:
            if age > 0 and age < 150:
                tupla = name, age
                return tupla
    except:
        pass
    raise ValueError
        
    
    
if __name__ == "__main__":
    print(new_person("Carnos groselhiane", 455))