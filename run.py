
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


def get_user_steps():
    """
    Get daily steps from the user for the past 7 days
    """
    while True:
        print("Please enter the daily step count for the past 7 days\n")
        print("The numbers must be entered in the the following format")
        print("7 numbers seperated by commas")
        print("Example: 100,2000,33,777,8585,6456,1456\n")

        user_steps = input("Enter your daily steps here: \n")

        user_steps_converted = user_steps.split(",")

        if validate_user_entry(user_steps_converted):
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
            raise ValueError(f"You have entered: {len(values)} numbers \n")
    except ValueError as error:
        print(f"\nInvalid data entered: {error}")
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
    data_steps_worksheet = SHEET.worksheet("steps").get_all_values()
    weeks = len(data_steps_worksheet) - 1

    sum_this_week = sum(weekly_steps_converted)
    avarage_this_week = int(sum_this_week / 7)
    print(f"You have walked total of {sum_this_week} steps this week")
    print(f"Your daily avarage is: {avarage_this_week} steps.")

    if weeks <= 1:
        print("Only one week of data available")
        print("Come back next week to compare the results.\n")
    else:
        previous_week = data_steps_worksheet[-2]
        converted_prev_week = [int(string) for string in previous_week]
        sum_prev_week = sum(converted_prev_week)
        avg_prev_week = sum_prev_week / 7
        difference = sum_this_week - sum_prev_week
        avg_diff = avarage_this_week - avg_prev_week
        if difference < 0:
            compare = "less"
        else:
            compare = "more"
        if avg_diff < 0:
            avg_compare = "less"
        else:
            avg_compare = "more"
        print(f"You have walked {difference} {compare}")
        print("than the previous week\n")
        print(f"Your avarage daily steps last week was: {int(avg_prev_week)}")
        print(f"That is {int(avg_diff)} {avg_compare} ")
        print("daily avarage steps than last week!\n")
    ask_bmr_question()
    return sum_this_week


def ask_bmr_question():
    """
    Find from the user if they want to find out
    total calorie requirments based on their stats.
    """
    print("Would you like to find out your BMR?\n")
    print("Your Basal Metabolic Rate (BMR) is the number of calories you burn")
    print(" as your body performs basic (basal) life-sustaining functions.")
    print("Commonly also called as Resting Metabolic Rate (RMR),")
    print("which is the calories burned if you stayed in bed all day.\n")


def get_user_stats():
    """
    Get data from the user.
    """
    user_choice = input("Please type 'yes' or 'no': ").lower()
    if user_choice == "yes":
        while True:
            height = input("Enter your height in cm(e.g: 176):\n")
            if validate_number(height):
                break
        while True:
            print("Please enter your weight in kg,")
            weight = input("without a decimal point:\n")
            if validate_number(weight):
                break
        while True:
            age = input("Enter your age:\n")
            if validate_number(age):
                break
        while True:
            print("Please enter 'm' for a man,")
            gender = input("or 'w' if you are a woman: \n").lower()
            if gender == "m" or gender == "w":
                print("Thank you, data entered correctly!\n")
                break
            else:
                print("Please enter 'm' for a man,")
                gender = input("or 'w' if you are a woman: \n").lower()
        calculate_bmr(height, weight, age, gender)
    elif user_choice == "no":
        print("No, problem. Please return next week with more step data.")
        exit()
    else:
        get_user_stats()


def validate_number(string):
    """
    Validate if the data entered is a positive number
    """
    try:
        number = int(string)
        if number > 0:
            print("Thank you")
        else:
            print("that's not a positive number. Try again: ")
            return False
    except ValueError:
        print("This is not a valid number, try again: ")
        return False
    return True


def calculate_bmr(height, weight, age, gender):
    """
    Calculate the BMR using different formula
    depending on the gender
    """
    weight = int(weight)
    height = int(height)
    age = int(age)
    if gender == "m":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "w":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    print(f"\nYour BMR is: {int(bmr)} per day.\n")
    print("---------------------------------------------")
    print("Hope the data insigths were useful to you!")
    print("We challenge you to get more steps next week!")
    print("See you soon!")
    print("---------------------------------------------")


def update_steps_worksheet(values):
    """
    Add weekly steps values to the google worksheet
    Add new row for each week
    """
    steps_worksheet = SHEET.worksheet("steps")
    steps_worksheet.append_row(values)
    print("Database updated successfully.\n")


def main():
    """
    Run all main functions
    """
    weekly_steps = get_user_steps()
    weekly_steps_converted = [int(step) for step in weekly_steps]
    update_steps_worksheet(weekly_steps_converted)
    current_weeks_steps = calculations(weekly_steps_converted)
    get_user_stats()

print("---------------------------------------------------------")
print("Welcome to WalkActive!")
print("This tool is designed to keep you aacountable")
print("provide feedback of your weekly activity levels")
print("and motivate you to move more.")
print("Enter data every week, and see how you improve over time.")
print("There will also be an option to find out your BMR\n")
print("----------------------------------------------------------")
main()
