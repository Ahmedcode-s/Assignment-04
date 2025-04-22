PROMPT: str = "What do you want?"
JOKE: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
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