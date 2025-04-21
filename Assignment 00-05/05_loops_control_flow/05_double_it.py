max_value = 100

def main():
    user_input = int(input("Enter a number you want to double: "))
    
    
    while user_input < max_value:
       user_input = user_input*2
       print(user_input)

if __name__ == "__main__":
     main()
    