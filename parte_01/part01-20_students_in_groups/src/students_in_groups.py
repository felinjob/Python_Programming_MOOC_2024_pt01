# Write your solution here
students = int(input("How many students on the course? "))
groups = int(input("Desired group size? "))

if students % groups == 0:
    print("Number of groups formed:", students // groups)
elif students % groups != 0:
    print("Number of groups formed:", students // groups + 1)