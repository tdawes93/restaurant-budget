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

def input_bookings():

def add_bookings_to_spreadsheet():

def calculate_walkins():

def add_walkins_to_spreadsheet():

def calculate_takings():

def add_takings_to_spreadsheet():

def calculate_staff_numbers():

def add_staff_numbers_to_spreadsheet():

def main():
    
