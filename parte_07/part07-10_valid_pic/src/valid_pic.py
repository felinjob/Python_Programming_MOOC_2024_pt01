# Write your solution here
from string import ascii_uppercase, digits
from datetime import datetime, timedelta
    
def valid_datetime(pic: str):
    day = int(pic[:2])
    month = int(pic[2:4])
    if pic[6] == "-":
        year = int("18" + pic[4:6])
    elif pic[6] == "+":
        year = int("19" + pic[4:6])    
    elif pic[6] == "A":
        year = int("20" + pic[4:6])   
    else:
        return False
    try:
        return True if datetime(year, month, day) else False
    except ValueError:
        return False
    
def sep_values(pic: str):    
    try:
        numbers = int(pic[:6] + pic[7:10])
        return numbers
    except ValueError:
        return False
    
def calc_rem(numbers: int, pic: str):
    index = numbers % 31
    compare = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    
    if compare[index] == pic[-1]:
        return True
    else:
        return False
    
def is_it_valid(pic: str):
    if len(pic) > 11:
        return False
    if valid_datetime(pic) == True:
        numbers = sep_values(pic)
    else: 
        return False
    if calc_rem(numbers, pic) == True:
        return True
    else: 
        return False
if __name__ == "__main__":
    is_it_valid()