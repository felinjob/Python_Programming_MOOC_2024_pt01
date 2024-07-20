# Write your solution here
attempts = 0
pin = "4321"
while True:
    code = input("PIN: ")
    attempts += 1
    if code == pin:
        success = True
        break
    else: 
        print("Wrong")
if success:
    if attempts == 1:
        print("Correct! It only took  you one single attempt!")
    else:
        print(f"Correct! It took you {attempts} attempts")
        
