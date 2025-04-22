import random 

print("Think of a number between 1 - 10 and the computer will guess it.")

low = 1
high = 10

if low <= high:
    guess = random.randint(low,high)
    print("The computer's guess is:", guess)

    while True:
        feedback = input("Is the guess to high (H), too low (L) or is it correct (C)?").strip().upper()

        if feedback == "C":
            print("Yay! The Computer guessed your number.")
            break
        elif feedback == "H":
            high = guess - 1
            guess = random.randint(low ,high)
            print(f"Computer's guess is : {guess}")
        elif feedback == "L":
            low = guess - 1
            guess = random.randint(low ,high)
            print(f"Computer's guess is : {guess}")
        else:
            print("Invalid input. Please enter H,L, or C.")

if low > high:
    print("The number is not in the range. Please try again")
