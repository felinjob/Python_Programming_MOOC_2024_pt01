# Write your solution here
from datetime import datetime, timedelta
    
    
def how_old(day: int, month: int, year: int):
    
    born_in  = datetime(year, month, day)
    new_mill = datetime(1999, 12, 31)
    age_in = new_mill - born_in
    if born_in > new_mill:
        return "You weren't born yet on the eve of the new millennium."
    return f"You were {age_in.days} days old on the eve of the new millennium."
    
    
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
print(how_old(day, month, year))