# Write your solution here
def add_student(dictionary: dict, student: str):
    dictionary[student] = [("no completed courses",)]
    
def print_student(dictionary: dict, student: str):
    if student not in dictionary:
        print(f"{student}: no such person in the database")
    
    elif dictionary[student][0][0] == "no completed courses":
            print(student + ":")
            for lists in dictionary[student]:
                for value in lists:
                    print(f" {value}")
    
    else:
        print(f"{student}:\n {len(dictionary[student])} completed courses:")
        for lists in dictionary[student]:
            print("  ", end="")
            for index in range(len(lists)):
                print(f"{lists[index]}", end=" ")
            print()
        average = 0
        for lists in dictionary[student]:
            average += lists[-1]
        print(f" average grade {average/len(dictionary[student]):.1f}")
    
def compare_courses(dictionary: dict, student: str, course: tuple):
    
    for item in range(len(dictionary[student])):
        if course[0][0] == dictionary[student][item][0]:
            if course[0][1] > dictionary[student][item][1]:
                dictionary[student][item] = course[0]  
            return True            
    return False
def add_course(dictionary: dict, student: str, course: tuple):
    listnator = [course]
    if listnator[0][-1] == 0:
        return
    if dictionary[student][0][0] == "no completed courses":
        dictionary[student] = listnator
        return
    if compare_courses(dictionary, student, listnator):
        return    
    dictionary[student] += listnator
    
    
def summary(dictionary: dict):
    
    courses = 0
    most = ""
    average = 0
    best = ""
    for student in dictionary:
        if courses > len(dictionary[student]):
            break
        courses = len(dictionary[student])
        most = f"most courses completed {courses} {student}"
    for student in dictionary:
        soma = 0
        item = 0
        for itens in dictionary[student]:
            soma += itens[-1]
            item += 1  
        if (soma / item) >= average:
            average = (soma / item)
            best = f"best average grade {(soma / item):.1f} {student}"
    print(f"students {len(dictionary)}")
    print(most)
    print(best)
    
    
    
if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    print_student(students, "Emily")
    summary(students)
    summary(students)