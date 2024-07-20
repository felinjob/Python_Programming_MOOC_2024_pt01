# wwite your solution here
def students_dict(student: dict):
    with open(input("Students information: ")) as students_file:
        for line in students_file:
            parts = line.split(';')
            if parts[0] == "id":
                continue
            student[parts[0]] = f"{parts[1]} {parts[2].strip()}"
    
def exercises_dict(points: dict):
    with open(input("Exercises completed: ")) as points_file:
        for line in points_file:
            parts = line.split(';')
            name = parts[0]
            if name == "id":
                continue
            points[name] = []
            for notes in parts[1:]:        
                points[parts[0]].append(int(notes))
    
def exams_dict(points: dict):
    with open(input("Exam points: ")) as points_file:
        for line in points_file:
            parts = line.split(';')
            name = parts[0]
            if name == "id":
                continue
            points[name] = []
            for notes in parts[1:]:        
                points[parts[0]].append(int(notes))
    
    
def main():
    students = {}
    exercises = {}
    exam_points = {}
    
    students_dict(students)
    exercises_dict(exercises)
    exams_dict(exam_points)
    
    
    for pic, name in students.items():
        if pic in exercises:
            if pic in exam_points:
                grades =  exercises[pic]
                notes = exam_points[pic]
                finals = int(((sum(grades)/40 * 100 // 10) + sum(notes)))
                final_grade = 0
                if finals > 27:
                    final_grade = 5
                elif finals > 23:
                    final_grade = 4
                elif finals > 20:
                    final_grade = 3
                elif finals > 17:
                    final_grade = 2
                elif finals > 14: 
                    final_grade = 1
                elif finals <= 14:
                    final_grade = 0
    
                print(f"{name} {final_grade}")
    
    
    
    
main()