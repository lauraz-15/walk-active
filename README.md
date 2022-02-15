
## WalkActive

WalkActive is a Python terminal programme, that is designed to perform calculation in order to motivate user to be more active. 

There is also an option to calculate BMR - daily calories needs based on individuals weight, height, age and gender. 

Programme is deployed on Heroku which allows the programme to be accessible to anyone. 

Please Click [here](https://walk-active.herokuapp.com/) to access this project.

![Mock-up](https://github.com/lauraz-15/walk-active/blob/main/assets/readme_images/mock-up.png)

### How to use it?

When the program is launched user is introduced what the programme does. 
Then user must enter the date of the last 7days of daily steps. 
The data can be taken from any step counter app, most mobile phone will have this feature built in which allows mist users to use the programme straight away without any preparation/data collection. 


### Features


Once the data is entered in the correct format, data is uploaded to the Google sheets.
This lets the user the save weeks worth of date and compare the results with the previous weeks. 

If only one weeks of data will be provided, then total steps will be calculated for that week. The total steps are calculated for that week. This encourages the user to understand the activity level and motivates to achieve more the following week.

Extensive calculations are done if there is date available for the previous weeks. 
Such as the the difference of total weekly steps comparing to the previous week, which should encourage the user to get more active is the result is negative number or get even more steps if there is any improvement.

The results are then presented to the user, which should encourage the user to get more steps in the following week.

After the results are presented to the user, there is an option for a user to find out their BMR(Basal Metabolic rate (total number of calories that body needs to perform basic, life-sustaining functions. The result is based on users individual stats, so as the weight changes, metabolic rate would also change therefore user can recalculate the BMR each week(assuming there are weight changes.)
This feature would motivate the user to monitor their daily calotie intake and add extra steps if extra calories were consumed. 

### Bugs

There was a bug with user imput when capital letters were used. There loop worked  prompting the user to enter the answer again, but one the an

### Testing

Testing was performed to ensure that all programme runs as exected. All formulas and calculation were checked if correct. 
Extensive testing was performed for the user input asnwers. Some errors and bigs were found(marked in yellow below), then was fixed and retested.

![Mock-up](https://github.com/lauraz-15/walk-active/blob/main/assets/readme_images/mock-up.png)
![Mock-up](https://github.com/lauraz-15/walk-active/blob/main/assets/readme_images/mock-up.png)

### Validator Testing

Code was passed through PEP8 Python Validator - no errors found.

### Technologies

Project was created using Python Essentials template from Code Institute on Github:
[here](https://github.com/Code-Institute-Org/python-essentials-template) 

Project was built using **Gitpod**

**Python** was used as a programming language
The deployed using **Heroku**.
[**Google Drive**](https://drive.google.com/) and [**Google sheets API**](https://developers.google.com/sheets/api) 
was connected, so data can be collected and stored on Google spreadhseet.

The BMR fromulas were taken from [Diabetetes.co.uk)https://www.diabetes.co.uk/bmr-calculator.html

### Deployment

1. Create list of requirements by entering this command in the terminal: 
*pip3 freeze > requirements.txt*
2. Sign up to Heroku account
3. Click “add new app”
4. Go to “settings”
5. Click “Reveal Config Vars”
5. Add 2 keys with values as below:
	-Key: CREDS Value: (copy whole creds.json file)
	-Key: PORT, Value: 8000
6. Add build-packs: Python and node.js
7. Then go to Delpoy and select github
8. Search for GitHub repository and connect
9. Wait until project is deployed and click “View” when button shows up.pip3 freeze > requirements.txt 
10. Wait until project is deployed and click “View” when button shows up.