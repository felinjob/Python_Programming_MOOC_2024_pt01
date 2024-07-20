# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", "a") as edit_file:
        nome, idade, altura = person
        edit_file.write(f"{nome};{idade};{altura}\n")
    
if __name__ == "__main__":
    store_personal_data()