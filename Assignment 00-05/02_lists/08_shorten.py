Max_list : int = 3

def get_short(List):
    while len(List) > 3:
        value = List.pop()
        print(value)

#This Funtion is for asking the user to enter elements in the list:
def add_list():
    List = []
    user_input: str = input("Please enter an element of the list or press enter to stop:")
    while user_input != "":
        List.append(user_input)
        user_input = input("Please enter an element of the list or press enter to stop:")
    return List

def main():
    List = add_list()
    get_short(List)

if __name__ == '__main__':
    main()