# Write your solution here
def read():
    students = []
    with open("solutions.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            split = line.split(";")
            students.append(split)
    return students
    
def correct(student: list):
    with open("correct.csv", "a") as new_file:
        rejoined = ";".join(student)
        new_file.write(f"{rejoined}\n")
def incorrect(student: list):
    with open("incorrect.csv", "a") as new_file:
        rejoined = ";".join(student)
        new_file.write(f"{rejoined}\n")
    
def calc(students: list):
    with open("correct.csv", "w") as new_file:
        pass
    with open("incorrect.csv", "w") as new_file:
        pass
    lists = students
    for student in lists:
        name, operation, result = student
        for item in student:
            print()
        if "+" in operation:
            num1, num2 = operation.split("+")
            if int(num1) + int(num2) == int(result):
                correct(student)
            else:
                incorrect(student)
        elif "-" in operation:
            num1, num2 = operation.split("-")
            if int(num1) - int(num2) == int(result):
                correct(student)
            else:
                incorrect(student)
    
def filter_solutions():
    students = read()
    calc(students)
    
if __name__ == "__main__":
    filter_solutions()