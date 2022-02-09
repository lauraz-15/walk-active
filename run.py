
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('WalkActive')

sales = SHEET.worksheet('steps')

# data = sales.get_all_values()

# print(data)

def get_user_steps():
    """
    Get daily steps from the user for the past 7 days
    """
    print("Please enter the daily step count for the past 7 days\n")
    print("The numbers must be entered in the the following format")
    print("7 numbers seperated by commas")
    print("Example: 100, 2000, 33, 777, 8585, 6456, 1456\n")

    user_steps = input("Enter your daily steps here: \n")

    print(f"You have entered: {user_steps}")


get_user_steps()