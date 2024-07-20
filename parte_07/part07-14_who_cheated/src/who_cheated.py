# Write your solution here
import datetime as dt
    
def dictionary():
    start_times = {}
    with open("start_times.csv", "r") as start_file:
        with open("submissions.csv") as submissions:
            for line in start_file:
                
                student = line.split(";")
                name, hour = student
                hour = hour.strip()
                hour, minute = hour.split(":")
                started = dt.timedelta(hours= int(hour), minutes= int(minute))
                start = {"start": started}
    
                start_times[name] = start
            for line in submissions:
                line = line.replace("\n", "")
                student = line.split(";")
                name = student[0]
                hour, minute = student[-1].split(":")            
                ended = dt.timedelta(hours= int(hour), minutes= int(minute))
                diction = {"endtime": ended}
                if name in start_times:
                    if "endtime" not in start_times[name]:
                        start_times[name].update(diction)
                    if start_times[name]["endtime"] < diction["endtime"]:
                        start_times[name].update(diction)
    return start_times
    
def cheaters():
    start_times = {}
    with open("start_times.csv", "r") as start_file:
        with open("submissions.csv") as submissions:
            for line in start_file:
                
                student = line.split(";")
                name, hour = student
                hour = hour.strip()
                hour, minute = hour.split(":")
                started = dt.timedelta(hours= int(hour), minutes= int(minute))
                start = {"start": started}
    
                start_times[name] = start
            for line in submissions:
                line = line.replace("\n", "")
                student = line.split(";")
                name = student[0]
                hour, minute = student[-1].split(":")            
                ended = dt.timedelta(hours= int(hour), minutes= int(minute))
                diction = {"endtime": ended}
                if name in start_times:
                    if "endtime" not in start_times[name]:
                        start_times[name].update(diction)
                    if start_times[name]["endtime"] < diction["endtime"]:
                        start_times[name].update(diction)
    
    balisa = dt.timedelta(hours= 3, minutes= 0)
    name_list = []
    for name in start_times:
        if start_times[name]["endtime"] - start_times[name]["start"] > balisa:
            name_list.append(name)
    return name_list
    
if __name__ == "__main__":
    print(cheaters())