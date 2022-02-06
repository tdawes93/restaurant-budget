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


def input_bookings():
    """
    Get bookings figures inputted by user
    """
    print("Please enter your booking numbers for the week, Monday to Sunday")
    print("Data must be in the form of 7 numbers seperated by commas\n")

    bookings_input = input("Enter your data here: ")
    print(f"\nYou have entered your weekly booking numbers as {bookings_input}")
    bookings = [int(booking) for booking in bookings_input.split(",")]
    print(bookings)


# def add_bookings_to_spreadsheet():

# def calculate_walkins():

# def add_walkins_to_spreadsheet():

# def calculate_takings():

# def add_takings_to_spreadsheet():

# def calculate_staff_numbers():

# def add_staff_numbers_to_spreadsheet():

# def main():

input_bookings()

