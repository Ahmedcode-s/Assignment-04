import random

Sides = 6

def roll_dice():
    dice1 = random.randint(1 , Sides)
    dice2 = random.randint(1 , Sides)
    print( f"Dice 1 = {dice1}")
    print( f"Dice 2 = {dice2}\n")

for i in range(3):
    
    # #This line shows that dice1 is blocked scope variable and it doesnt affect the dice1 variable in roll_dice function.
    # dice1 = 10
    # print(f"Dice1 is still {dice1}")  
    
    i += 1
    print(f"Roll {i} :" )
    roll_dice()

