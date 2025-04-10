Peturksbouipo: int = 16
Stanlau: int = 25
Mayengua: int = 48 

def main():
    user_age = int(input("Please enter your age: "))
    if user_age >= Peturksbouipo:
        print("You can vote in  Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in  Peturksbouipo where the voting age is 16.")

    if user_age >= Stanlau:
        print("You can vote in  Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in  Stanlau where the voting age is 25.")
    
    if user_age >= Mayengua:
        print("You can vote in  Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in  Mayengua where the voting age is 48.")


if __name__ == '__main__':
    main()