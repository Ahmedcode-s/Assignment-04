min_height = 60

def main():
    user_age = int(input("Enter your height in inches:"))
    
   
    
    if user_age >= min_height:
        print("You are tall enough to ride!")
    else:
        print("You are not tall enough to ride :( ") 



if __name__ == '__main__':
    main()
