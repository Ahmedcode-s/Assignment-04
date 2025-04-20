def add_contact(phonebook):
    input_name = input("Enter contact name: ")
    input_number = input("Enter contact number: ")

    if input_name in phonebook:
        print(f"{input_name} already exits in the phonebook.")
    else:
        phonebook[input_name] = input_number
        print(f"{input_name} added to the phonebook.")

def search_contact(phonebook):
    name = input("Enter contact name to search:")

    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"{name} not found in the phonebook.")

def delete_contact(phonebook):
    name = input("Enter contact name to delete it: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted {name} from the phonebook. ")
    else:
        print(f"{name} not found in the phonebook.")

def display_contact(phonebook):
    if phonebook:
        print("\n Phonebook contact list: ")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty.")

if __name__ == "__main__":
    phonebook = {}

    while True:
        print("\n Phonebook : ")
        print("1. Add a Contact")
        print("2. Search a Contact")
        print("3. Delete a Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter the option you want to select (1-5): ")

        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_contact(phonebook)
        elif choice == "3":
            delete_contact(phonebook)
        elif choice == "4":
            display_contact(phonebook)
        elif choice == "5":
            print("Exiting Phonebook.... GOODBYE!")
            break
        else:
            print("Invalid option. Please enter the correct option mention between 1-5.")

    

