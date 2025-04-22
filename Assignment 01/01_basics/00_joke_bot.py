PROMPT: str = "What do you want?"
JOKE: str =" Why don't graveyards ever get overcrowded? Because people are dying to get in."
SORRY: str = "Sorry I only tell jokes. Type joke to get a laugh."

def main():
    print(PROMPT)
    user_input = input()
    user_input = user_input.strip().lower()
    
    while True:
        if "joke" in user_input:
            print(JOKE)
            break
        print(SORRY)
        user_input= input()
    
if __name__ == "__main__":
    main()