import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = (Credentials.from_service_account_file("creds.json"))
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
SHEET = gspread.authorize(SCOPED_CREDS).open("restaurant_budget")

# bookings = SHEET.worksheet("bookings")
# data = bookings.get_all_values()
# print(data)


def request_action():
    """
    Asks the user what action they wish to perform
    """
    while True:
        print("Do you wish to:")
        print("1. Enter a new booking")
        print("2. View total number of bookings")
        print("3. Calculate staff numbers required for following week\n")
        choice = input("Please type the number of your choice: ")

        if validate_request(choice):
            print(f"\nYou have selected {choice} is this correct? (Y/N)")
            check = input()
            if validate_check(check):
                if check == "Y" or check == "y":
                    print("\nYou have confirmed your answer\n")
                    break
                else:
                    print("\nPlease start again\n")

    return choice


def validate_request(value):
    """
    Takes the choice selected by the user and
    checks it's a valid answer
    """
    try:
        if value not in ("1", "2", "3"):
            raise ValueError("Input must be 1, 2 or 3")
    except ValueError as e:
        print(f"\nInvalid data: {e}, please try again.\n")
        return False
    return True


def validate_check(value):
    """
    Takes the confirmation input by the user
    and check's it's a valid answer
    """
    try:
        if value not in ("n", "y", "N", "Y"):
            raise ValueError("Input must be Y or N, please select again")
    except ValueError as e:
        print(f"Invalid data, {e}, please try again.\n")
        return False
    return True


def interpret_request(variable):
    """
    Takes the choice selected by the user and 
    works out which route they wish to proceed with
    """
    print(f"Loading option {variable}...\n")
    variable = int(variable)
    if variable == 1:
       input_booking()
    elif variable == 2:
        view_bookings()
    elif variable == 3:
        calculate_staff_numbers()
    else:
       print("You have selected an unavailable option. Please start again")


def input_booking():
    """
    Get bookings inputted by user
    """
    while True:
        day = input("Please enter the day of your booking here: ")
        if validate_day(day):
            print(f"You have selected {day}")
    # bookings_input = input("Enter your data here: ")
    # print(f"\nYou have entered your weekly bookings as {bookings_input}")
    # return bookings_input
    # bookings = [int(d) for d in data.split(",")]


def validate_day(day):
    """
    Takes the day entered by the user and 
    checks it's valid
    """
    try:
        if day not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
            raise ValueError("Input must be a day of the week with a capital letter")
    except ValueError as e:
        print(f"\nInvalid data: {e}, please try again.\n")
        return False
    return True

    
# def validate_bookings(data):
    # """
    # Check the inputted data meets the requirements and
    # if not returns an error message
    # """
    # try:
        # for d in data:
            # if 0 > d or d < 100:
                # raise ValueError(
                    # "Number of bookings must be between 0 and 100")
    # except ValueError():
        # print("Values must be numerical between 0 and 100")

# def add_bookings_to_spreadsheet():

# def calculate_walkins():

# def add_walkins_to_spreadsheet():

# def calculate_takings():

# def add_takings_to_spreadsheet():

# def calculate_staff_numbers():

# def add_staff_numbers_to_spreadsheet():


def main():
    """
    Runs the main functions of the python code
    """
    request = request_action()
    interpret_request(request)
    # validate_request(request)
    # bookings_data = input_bookings()
    # validate_bookings(bookings_data)


main()

