# Write your solution here
import json
    
def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()
    
        people = json.loads(data)
        for person in people:            
            hobbie = ", ".join(person["hobbies"])
            hobbie = f"({hobbie})"
            print(person["name"], person["age"], "years", hobbie)
    
    
if __name__ == "__main__":
    print_persons("file1.json")