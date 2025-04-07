#I added the user input part for fun it wasnt in the assignment ;)


day_in_year: int = 365
hour_in_day: int = 24
min_in_hour: int = 60
sec_in_min: int = 60

def main():
    user_year: int = int(input("Enter the number of year you want in seconds: "))
    
    day_in_year: int = 365*user_year
    
    convert_year_in_sec = (((day_in_year*hour_in_day)*min_in_hour)*sec_in_min)

    print(f"There are {convert_year_in_sec} seconds in {user_year} years")


if __name__ == '__main__':
    main()