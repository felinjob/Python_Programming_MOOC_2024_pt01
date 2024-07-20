# write your solution here
names = {}
grades = {}
    
with open(input("Student information: ")) as full_names:
    valor = full_names
    with open(input("Exercises completed: ")) as all_grades:
        for line in full_names:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            names[parts[0]] = f"{parts[1] } {parts[2].strip()}"
        for line in all_grades:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            grades[parts[0]] = []
            for grade in parts[1:]:
                grades[parts[0]].append(int(grade))
    
for pic, name in names.items():
            if pic in grades:
                grade = grades[pic]
                print(f"{name} {sum(grade)}")