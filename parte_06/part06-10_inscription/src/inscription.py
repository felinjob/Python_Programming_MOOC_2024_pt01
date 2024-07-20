# Write your solution here
name = input("Whom should I sign this to: ")
save = input("Where shall I save it: ")
with open(save, "w") as my_file:
    my_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")



