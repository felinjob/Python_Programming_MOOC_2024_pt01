# Write your solution here
import urllib.request, json
    
def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    
    courses = json.loads(my_request.read())
    loT = []
    
    for course in courses:
        if course["enabled"] == True:
            exercises = sum(course["exercises"])
            lists = (course["fullName"], course["name"], course["year"], exercises)
            loT.append(lists)
    return loT
    
def retrieve_course(course_name: str):
    course_url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats"
    course_request = urllib.request.urlopen(course_url)
    course_info = json.loads(course_request.read())
    
    weeks = len(course_info)
    students = 0
    hours = 0    
    exercises = 0
    
    for key in course_info:
    
        for item in course_info[key]:
            if item == "students":
                if course_info[key][item] > students:
                    students = course_info[key][item]
            elif item == "hour_total":
                hours += course_info[key][item]
            elif item == "exercise_total":
                exercises += course_info[key][item]
    
    hours_average = hours // students
    exercises_average = exercises // students
    course = {'weeks': weeks, 'students': students, 'hours': hours, 'hours_average': hours_average, 'exercises': exercises, 'exercises_average': exercises_average}
    
    return course  
            
    
    
if __name__ == "__main__":
    retrieve_all()
    retrieve_course()