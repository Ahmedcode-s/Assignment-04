import random

def guess_num():

    random_num = random.randint(1 ,99)

    print("Im thinking of a number betweeen 1-99.......")

    user_guess = int(input("Enter your guess:"))

    while user_guess != random_num:
        if user_guess > random_num:
            print("Your guess is high.")
        elif user_guess < random_num:
            print("Your guess is low.")

        print()
        user_guess = int(input("Enter your new guess:"))

    print(f"You got it! The number was : {random_num}")

if __name__ == '__main__':
    guess_num()   

