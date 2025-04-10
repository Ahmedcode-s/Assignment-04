def get_last_elem(lst):
    print(lst[len(lst)-1])

#This Funtion is for asking the user to enter elements in the list:
def add_list():
    List = []
    user_input: str = input("Please enter an element of the list or press enter to stop:")
    while user_input != "":
        List.append(user_input)
        user_input = input("Please enter an element of the list or press enter to stop:")
    return List

# This function runs the main logic: it gets the list from the user and prints the first element.
def main():
    List = add_list()
    get_last_elem(List)

if __name__ == '__main__':
    main()
