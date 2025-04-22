import random

print("Lets play rock, paper, scissors game!")

game_options = ["rock" ,"paper","scissor"]
user_score = computer_score = 0

while True:
    user_input = input("Type Rock, Paper, Scissor or Q to quit: ").lower()

    if user_input == "q":
        print("Thanks for playing")
        print(f"Final score -  you:{user_score} , computer:{computer_score}")
        break
    if user_input not in game_options:
        print("Invalid input, Please try again.")
        continue
    computer_choice = random.choice(game_options)
    print(f"Computer chose: {computer_choice}")
    if user_input == game_options:
        print("Its a tie!")
    elif (user_input == "rock" and computer_choice == "scissor") or \
            (user_input == "paper" and computer_choice == "rock") or \
            (user_input == "scissor" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1

    print(f"Current Score - you:{user_score} , computer:{computer_score}")