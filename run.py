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
    print("Do you wish to:")
    print("1. Enter a new booking")
    print("2. View total number of bookings")
    print("3. Calculate staff numbers required for following week\n")
    choice = input("Please type the number that corresponds to your choice: ")
    return choice


def validate_request(value):
    """
    Take the choice selected by the user and
    checks it's a valid answer
    """
    try:
        int(value)
    except ValueError as e:
        print(f"\nInvalid data: {e}, please try again.\n")
        main()


# def input_bookings():
    # """
    # Get bookings figures inputted by user
    # """
    # print("Please enter your booking numbers for the week, Monday to Sunday")
    # print("Data must be in the form of 7 numbers seperated by commas\n")

    # bookings_input = input("Enter your data here: ")
    # print(f"\nYou have entered your weekly bookings as {bookings_input}")
    # return bookings_input
    # bookings = [int(d) for d in data.split(",")]


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
    validate_request(request)
    # bookings_data = input_bookings()
    # validate_bookings(bookings_data)


main()

