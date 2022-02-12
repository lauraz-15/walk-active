
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
            raise ValueError(f"You have entered: {len(values)}\n")
    except ValueError as e:
        print(f"\nInvalid data entered: {e}")
        print("Read the instructions and try again! \n")
        get_user_steps()
        return False
    return True   


def calculations(weekly_steps_converted):
    """
    Check if there is weekly steps entered for the prevous weeks
    Get the data from the previous weeks
    Calculate total steps that week
    Calculate how many calories burned
    Compare the numbers with the prevous week
    """
    print("Please wait while the data is beeing processed")
    data_steps_worksheet = SHEET.worksheet("steps").get_all_values()
    weeks = len(data_steps_worksheet) - 1
    print(f"There are {weeks} weeks of data on the spreadhseet\n")
    sum_this_week = sum(weekly_steps_converted)
    print(f"You have walked total of {sum_this_week} steps this week")

    if weeks <= 1:
        print("Only one week of data available")
        print("Come back next week to compare the results")
    else:
        previous_week = data_steps_worksheet[-2]
        converted_prev_week = [int(string) for string in previous_week]
        sum_prev_week = sum(converted_prev_week)
        difference = sum_this_week - sum_prev_week
        if difference < 0:
            more_or_less = "less"
        else: 
            more_or_less = "more"
        print(f"This is {difference} {more_or_less} than the previous week")
    return sum_this_week


def calulate_calories(this_week):
    """
    Find from the user if they want to find out
    total calories burned based on their stats
    Calculate total calories burned
    """
    print(f"We have successfully imported stats: this week: {this_week}")
    user_choice = input("Would you like to find out how many calories that is based on your stats?")
    if user_choice == "yes":
        while True:
            height = input("Enter your height in cm(e.g: 176)\n")
            if validate_height_weight(height):
                break
        print("You have enetered valid number for your height")
        weight = input("Enter your weight in kg\n")
        print(f"You have entered Height: {height} & weight: {weight} \n Thank you!")
    elif user_choice == "no":
        print ("On avarage that woudl mean you have burned xx many calories")
    else: 
        print("Please answer with a 'yes'or 'no'")
        user_choice = input("Would you like to find out how many calories that is based on your stats?")


def validate_height_weight(string):
    """
    Validate if the data entered is a positive number
    """
    try:
        number = int(string)
        if number > 0:
            goodinput = True
            print("that's a good number. Well done!")
        else:
            print("that's not a positive number. Try again: ")
            return False
    except ValueError:
        print("This is not a number, try again: ")
        return False
    return True


def update_steps_worksheet(values):
    """
    Add weekly steps values to the google worksheet
    Add new row for each week
    """
    steps_worksheet = SHEET.worksheet("steps")
    steps_worksheet.append_row(values)
    print("Database updated successfully.\n")




#       1,22,33,55,55,66,99
#       800,900,800,600,800,700,52

#       python3 run.py

def main():
    """
    Run all main functions
    """
    weekly_steps = get_user_steps()
    weekly_steps_converted = [int(step) for step in weekly_steps]
    update_steps_worksheet(weekly_steps_converted)
    current_weeks_steps = calculations(weekly_steps_converted)
    calulate_calories(current_weeks_steps)

main()
