def add_copies(List , input):
    for i in range(3):
        List.append(input)

def main():
    user_input = input("Enter a message to copy:")
    List = []
    print("List Before:", List)
    add_copies(List , user_input)
    print("List After:", List)

if __name__ == "__main__":
    main() 