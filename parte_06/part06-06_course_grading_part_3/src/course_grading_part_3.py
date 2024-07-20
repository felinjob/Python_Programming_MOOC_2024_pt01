# tee ratkaisu tänne
student_data = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
    
# student_data = "students1.csv"
# exercise_data = "exercises1.csv"
# exam_data = "exam_points1.csv"
    
def grade(points):
    a = 0
    limits = [15, 18, 21, 24, 28]
    while a < 5 and points >= limits[a]:
        a += 1
    
    return a
    
def to_points(number):
    return number // 4
    
students = {}
with open(student_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2].strip()}"
    
exercises = {}
with open(exercise_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue
        esum = 0
        for i in range(1, 8):
            esum += int(parts[i])
        exercises[parts[0]] = esum
    
exams = {}
with open(exam_data) as file:
    for row in file:
        parts = row.split(";")
        if parts[0] == "id":
            continue 
        esum = 0
        for i in range(1, 4):
            esum += int(parts[i])
        exams[parts[0]] = esum
ref_list = ["name", "exec_nbr", "exec_pts.", "exm_pts.", "tot_pts.", "grade"]
print(f"{ref_list[0]:30}{ref_list[1]:10}{ref_list[2]:10}{ref_list[3]:10}{ref_list[4]:10}{ref_list[5]:10}")
    
for student_id, name in students.items():
    total = exams[student_id] + to_points(exercises[student_id])
    print(f"{name:30}{str(exercises[student_id]):10}{str(to_points(exercises[student_id])):10}{str(exams[student_id]):10}{str(total):10}{str(grade(total)):10}")



