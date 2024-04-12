import random

print("Welcome to the Dice Game!")
print("USAGE: The number must be between 1 and 8")
number = int(input("Enter the number of dice you want to roll: "))
j = 0

if number in range(1, 8):
    for i in range(number):
        dice_roll = random.randint(1, 6)
        j = j + dice_roll
        print("Dice",i+1,':',dice_roll)
    print("==========")
    print("Result:",j)
else:
    print("Invalid Number")


