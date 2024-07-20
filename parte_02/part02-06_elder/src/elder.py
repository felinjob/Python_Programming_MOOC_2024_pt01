# Write your solution here
print("Person 1:")
n_p1 = input("Name: ")
age_p1 = int(input("Age: "))
print("Person 2:")
n_p2 = input("Name: ")
age_p2 = int(input("Age: "))

if age_p1 == age_p2:
    print(f"{n_p1} and {n_p2} are the same age")
elif age_p1 > age_p2:
    print(f"The elder is {n_p1}")
else: 
    print(f"The elder is {n_p2}")
