def mad_lib():
    print("Let's make a silly sentence!")

    name = input("Enter a name: ")
    food = input("Enter a food: ")
    verb = input("Enter a verb ending in -ing: ")
    animal = input("Enter an animal: ")

    print("\nHere's your silly sentence:")
    print(f"{name} was {verb} while eating {food} with a {animal}. 😂")


if __name__ == "__main__":
    mad_lib()
