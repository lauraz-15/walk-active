
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

    user_steps_converted = user_steps.split(",")

    validate_user_entry(user_steps_converted)
    




def validate_user_entry(data):
    """
    Check if exaclty 7 numbers entered
    check if all 7 numbers are valid numbers
    """
    try:
        if len(data) != 7:
            raise ValueError(
                f"Exaclty 7 numbers expeced, you have entered {len(data)}"
            )
    except ValueError as e:
        print(f"Invalid data entered: {e}, read the instructions and try again! \n")
        get_user_steps()
        

get_user_steps()


# 1,22,33,55,55,66,99 
# python3 run.py