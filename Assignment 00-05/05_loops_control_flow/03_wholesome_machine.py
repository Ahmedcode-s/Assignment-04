correct_affirmation : str = "I am capable of doing anything I put my mind to."


def main():
    print(f"Please enter the following affirmation : {correct_affirmation}")
    user_input = input()

    while user_input != correct_affirmation:
        print("That is not the correct affirmation")

        print(f"Please enter the following affirmation : {correct_affirmation}")
        user_input = input()

    print("That's Right !")
        
        
if __name__  == "__main__":
    main()
