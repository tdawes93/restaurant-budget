import gspread
from google.oauth2.service_account import Credentials
import statistics
import math

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
            check = input().capitalize()
            if validate_check(check):
                if check == "Y":
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
        if value not in ("N", "Y"):
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
        booking = input_booking()
        print("\nProcessing booking...")
        print(f"\nThank you for making a booking.\nYour booking: {booking}")
        add_booking_to_spreadsheet(booking)
    elif variable == 2:
        weekly_bookings = view_bookings()
        print(f"Upcoming bookings this week:\n{weekly_bookings}")
    elif variable == 3:
        calculate_staff_numbers()
    else:
        print("You have selected an unavailable option. Please start again")


def input_booking():
    """
    Get bookings inputted by user
    """
    while True:
        print("Please enter the day of your booking.")
        print("It must be entered with the full word")
        print("E.g. Monday, Tuesday\n")
        day = input("Please enter the day of your booking here: ").capitalize()
        if validate_day(day):
            print(f"You have selected {day}")
            break
    while True:
        print("Please enter the number of people in your booking")
        print("We do not accept tables of more than 10\n")
        people = input("Please enter here: ")
        if validate_people(people):
            print(f"\nYou have selected {people} people")
            break
    day_of_booking = []
    day_of_booking.append(day)
    people = int(people)
    booking = dict.fromkeys(day_of_booking, people)
    return booking
    # bookings_input = input("Enter your data here: ")
    # print(f"\nYou have entered your weekly bookings as {bookings_input}")
    # return bookings_input
    # bookings = [int(d) for d in data.split(",")]


def validate_day(day):
    """
    Takes the day entered by the user and
    checks it's valid
    """
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"]
    try:
        if day not in days_of_week:
            raise ValueError("Input must be a day of the week")
    except ValueError as e:
        print(f"\nInvalid data: {e}, please try again.\n")
        return False
    return True


def validate_people(number):
    """
    Takes the number of people inputted in input bookings
    function and checks the input is valid
    """
    try:
        number = int(number)
        if 1 <= number <= 10:
            return True
        raise ValueError("Number of people must be between 1 and 10")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        return False


def view_bookings():
    """
    Retreives the most up to date data from the bookings
    worksheet and displays this weeks bookings to the user
    """
    bookings = SHEET.worksheet("bookings").get_all_values()
    this_weeks_bookings = [int(n) for n in bookings[-1]]
    days = bookings[0]
    weekly_bookings = dict(zip(days, this_weeks_bookings))
    return weekly_bookings


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


def add_booking_to_spreadsheet(booking):
    """
    Takes the dictionary of the booking made by the user
    and saves it to the worksheet 'bookings'
    """
    print("Do you wish to save your booking? (Y/N)")
    check = input().capitalize()
    if validate_check(check):
        if check == "Y":
            print("\nSaving booking...\n")
            day = list(booking.keys())[0]
            number = list(booking.values())[0]
            bookings_worksheet = SHEET.worksheet("bookings")
            bookings_data = bookings_worksheet.get_all_values()
            number_row = [int(b) for b in bookings_data[-1]]
            bookings_col = bookings_worksheet.col_values(1)
            bookings_worksheet.delete_rows(len(bookings_col))
            if day == "Monday":
                num = [number, 0, 0, 0, 0, 0, 0]
                r = [x + y for x, y in zip(number_row, num)]
                bookings_worksheet.append_row(r)
            elif day == "Tuesday":
                num = [0, number, 0, 0, 0, 0, 0]
                r = [x + y for x, y in zip(number_row, num)]
                bookings_worksheet.append_row(r)
            elif day == "Wednesday":
                num = [0, 0, number, 0, 0, 0, 0]
                r = [x + y for x, y in zip(number_row, num)]
                bookings_worksheet.append_row(r)
            elif day == "Thursday":
                num = [0, 0, 0, number, 0, 0, 0]
                r = [x + y for x, y in zip(number_row, num)]
                bookings_worksheet.append_row(r)
            elif day == "Friday":
                num = [0, 0, 0, 0, number, 0, 0]
                r = [x + y for x, y in zip(number_row, num)]
                bookings_worksheet.append_row(r)
            elif day == "Saturday":
                num = [0, 0, 0, 0, 0, number, 0]
                r = [x + y for x, y in zip(number_row, num)]
                bookings_worksheet.append_row(r)
            elif day == "Sunday":
                num = [0, 0, 0, 0, 0, 0, number]
                r = [x + y for x, y in zip(number_row, num)]
                bookings_worksheet.append_row(r)
        else:
            print("\nBooking deleted\n")


def calculate_staff_numbers():
    """
    Function that runs other functions to calculate how
    many staff are required to work for the upcoming week
    """
    print(
        "You are about to calculate the required number of staff for the week"
        )
    print("Have you entered all your bookings for the week? (Y/N)")
    check = input().capitalize()
    validate_check(check)
    if check == "Y":
        print("Calculating number of staff required for the upcoming week...")
        average_walkins = calculate_walkins()
        add_walkins_to_spreadsheet(average_walkins)
        # takings_data = calculate_takings()
        # add_takings_to_spreadsheet(takings_data)
        # staff_data = calculate_staff_required()
        # add_staff_numbers_to_spreadsheet(staff_data)
    else:
        print("Please finish entering your bookings")


def calculate_walkins():
    """
    Takes the last 10 weeks walkin numbers for each day
    and averages them, predicting the number of walkins
    for the upcoming week
    """
    walkin_data = SHEET.worksheet("walkins").get_all_values()
    days_of_week = walkin_data[1]
    average_walkins = []
    for i in range(1, (len(days_of_week) + 1)):
        daily_walkins = SHEET.worksheet("walkins").col_values(i)
        last_10_weeks_str = (daily_walkins[-10:])
        last_10_weeks = [int(walkin) for walkin in last_10_weeks_str]
        average_walkins_by_day = math.ceil(statistics.fmean(last_10_weeks))
        average_walkins.append(average_walkins_by_day)
    return average_walkins


def add_walkins_to_spreadsheet(walkin_data):
    """
    Takes the average walkins and adds the list to the google sheets
    """
    walkins_worksheet = SHEET.worksheet("walkins")
    walkins_worksheet.append(walkin_data)


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

