

def main():
    List = []
    user_input: str = input("Please enter a value: ")
    
    while user_input != "":
        List.append(user_input)
        user_input = input("Please enter a value: ")
    
    print(f"This is your list: {List}")

if __name__ == '__main__':
    main()