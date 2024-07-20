# Write your solution here
def exam_points(exam_points: str):
    exam_list = []
    
    for point in exam_points:
        exam_list.append(int(point.split(" ")[0]))
    return exam_list
 
def exercise_points(exercise_points: str):
    exercise_list = []
    for point in exercise_points:
        exercise_list.append((int(point.split(" ")[1])) * 100 // 100 // 10)
    return exercise_list
 
 
def average_points(exam: list, exercise: list):
    average = (sum(exam) + sum(exercise)) / len(exam)
    return (f"{average:.1f}")
 
def approved_list(exam_points: int, exercise_points: int):
    approved = []
    index = 0
    while index < len(exam_points):
        perc = exam_points[index] + exercise_points[index]
        if exam_points[index] >= 10:
            if perc >= 15:
                approved.append(perc)
        index += 1
    return approved
 
def reproved_list(exam_points: int, exercise_points: int):
    reproved = []
    index = 0
    while index < len(exam_points):
        perc = exam_points[index] + exercise_points[index]
        if exam_points[index] < 10 or perc < 15:
                reproved.append(perc)
        index += 1
    return reproved
 
def pass_perc(approveds: list, reproveds: list):
    approveds_perc = len(approveds) * 100 / (len(approveds) + len(reproveds))
    return (f"{approveds_perc:.1f}")
 
def grade_distribution(approveds: list, reproveds: list):
    five = ""
    four = ""
    three = ""
    two = ""
    one = ""
    zero = "*" * len(reproveds)
    for i in approveds:
        if i >= 28:
            five += "*"
        elif i >= 24:
            four += "*"
        elif i >= 21:
            three += "*"
        elif i >= 18:
            two += "*"
        elif i >= 15:
            one += "*"
    return (f"  5: {five} \n  4: {four} \n  3: {three} \n  2: {two} \n  1: {one} \n  0: {zero}")
 
def main():
 
    points_list = []
    while True:
        point_input = input("Exam points and exercises completed: ")
        if point_input == "":
            break
        points_list.append(point_input)
 
 
    exam_p = exam_points(points_list)
    exercise_p = exercise_points(points_list)
    average_p = average_points(exam_p, exercise_p)
    approved_total = approved_list(exam_p, exercise_p)
    reproved_total = reproved_list(exam_p, exercise_p)
    approved_percentage = pass_perc(approved_total, reproved_total)
    grade_dist = grade_distribution(approved_total, reproved_total)
 
    print("Statistics:")
    print(f"Points average: {average_p}")
    print(f"Pass percentage: {approved_percentage}")
    print("Grade distribution:")
    print(grade_dist)
 
 
main()