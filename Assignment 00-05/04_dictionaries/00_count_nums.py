def count_numbers():
    count_dict = {}

    while True:
        user_input = (input("Enter a number or type Exit to quit: "))
        if user_input.lower() == 'Exit':
            break
        if user_input.isdigit():
           user_input = int(user_input)
           count_dict[user_input] = count_dict.get(user_input , 0) + 1
           print(count_dict)
        else:
            print("Invalid input. Please enter a number")
            return count_dict
    
def display_count(count_dict):
    print("\n Number Counts:")
    for key, value in count_dict.items():
        print(f"{key} appears {value} times")

if __name__ == "__main__":
    counts = count_numbers()
    display_count(counts) 

