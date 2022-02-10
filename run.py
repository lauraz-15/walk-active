
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
    while True:
        print("Please enter the daily step count for the past 7 days\n")
        print("The numbers must be entered in the the following format")
        print("7 numbers seperated by commas")
        print("Example: 100, 2000, 33, 777, 8585, 6456, 1456\n")

        user_steps = input("Enter your daily steps here: \n")

        user_steps_converted = user_steps.split(",")

        if validate_user_entry(user_steps_converted):
            print("You have entered information in the correct format!")
            break
        
    return user_steps_converted


def validate_user_entry(values):
    """
    Check if exaclty 7 numbers entered
    check if all 7 numbers are valid numbers
    """
    try:
        [int(value) for value in values]
        if len(values) != 7:
            raise ValueError(f"Exactly 7 numbers expected, you have entered: {len(values)}")
    except ValueError as e:
        print(f"\nInvalid data entered: {e}, read the instructions and try again! \n")
        get_user_steps()
        return False

    return True   


def update_steps_worksheet(values):
    """
    Add weekly steps values to the google worksheet
    Add new row for each week
    """
    print("Updating weekly steps to the database...\n")
    steps_worksheet = SHEET.worksheet("steps")
    steps_worksheet.append_row(values)
    print("Database updated successfully.\n")


# 1,22,33,55,55,66,99

# python3 run.py

weekly_steps = get_user_steps()
weekly_steps_converted = [int(step) for step in weekly_steps]
update_steps_worksheet(weekly_steps_converted)