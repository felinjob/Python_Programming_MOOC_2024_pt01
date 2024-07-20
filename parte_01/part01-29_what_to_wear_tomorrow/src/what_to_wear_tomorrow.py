# Write your solution here
print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
v_rain = False
if rain == "yes":
    v_rain = True


if temperature > 20:
    print("Wear jeans and a T-shirt")
    if v_rain:
        print("Don't forget your umbrella!")
elif temperature > 10:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    if v_rain:
        print("Don't forget your umbrella!")
elif temperature > 5:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    if v_rain:
        print("Don't forget your umbrella!")
else:
    print("Wear jeans and a T-shirt")
    print("I recommend a jumper as well")
    print("Take a jacket with you")
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
    if v_rain:
        print("Don't forget your umbrella!")
