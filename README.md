
## WalkActive

WalkActive is a Python terminal programme, that is designed to perform calculation in order to motivate user to be more active. 

There is also an option to calculate BMR - daily calories needs based on individuals weight, height, age and gender. 

Programme is deployed on Heroku which allows the programme to be accessible to anyone. 

Please Click [here](https://walk-active.herokuapp.com/) to access this project.

![Walk-through-gif](https://github.com/lauraz-15/walk-active/blob/main/assets/readme_images/walk-active.gif)

### How to use it?

When the program is launched user is introduced what the programme does. 
Then user must enter the date of the last 7days of daily steps. 
The data can be taken from any step counter app, most mobile phone will have this feature built in which allows most users to use the programme straight away without any preparation/data collection. 


### Features


Once the data is entered in the correct format, data is uploaded to the Google sheets.
This lets the user the save many weeks worth of data or daily steps and compare the results with the previous weeks. 

If there is only one weeks worth of data available, then total steps and the avarage daily steps will be calculated for that week only. This encourages the user to understand thei activity level and motivates to achieve more the in the following week.

![One-week](https://github.com/lauraz-15/walk-active/blob/main/assets/readme_images/one-week.png)

Extensive calculations are done if there are data available for the previous weeks. 
Such as the the difference of total weekly steps comparing to the previous week, daily avarage this week and previous week, comparisation between the two. The results should encourage the user to get more active if the result is negative number or get even more steps in if the result is positive. Just by beeing aware of the numbers, should encourage the user for healthier choices (take steps instead of lift etc.)

![more-weeks](https://github.com/lauraz-15/walk-active/blob/main/assets/readme_images/more-weeks.png)

The results are then presented to the user, which should encourage the user to get more steps in the following week.

After the results are presented to the user, there is an option for a user to find out their BMR(Basal Metabolic rate (total number of calories that body needs to perform basic, life-sustaining functions. The result is based on users individual stats, so as the weight changes, metabolic rate would also change therefore user can recalculate the BMR each week(assuming there are weight changes.)
This feature would motivate the user to monitor their daily calotie intake and add extra steps if extra calories were consumed.

![more-weeks](https://github.com/lauraz-15/walk-active/blob/main/assets/readme_images/bmr.png)

### Flowchart

Flowchart was used in order to plan the project and order of functions.
Originally the idea was to calculate total calories burned per total weekly calories. However, the formula to calculate acurrate data was impossible to do, unles we would know the speed per hour for all steps teaken. most users would have different walking speeds thrughout the day depending on the activity.
Therefore for simplicity, this was replaced to calculate BMPR instead as additional bonus. 
However, this feature could be implemented in the future as advance feature for the users who would have the data available.

![flowchart]https://github.com/lauraz-15/walk-active/blob/main/assets/readme_images/flow-chart.png

### Bugs

There was a bug with user imput when capital letters were used. There loop worked prompting the user to enter the answer again, but one the correct value was entered programme stopped running. This was fixed using lower() method and fixing the flowchart loop.

### Testing

Testing was performed to ensure that all programme runs as exected. All formulas and calculation were checked if correct. 
Extensive testing was performed for the user input asnwers. Some errors and bugs were found(marked in yellow below), then was fixed and retested to ensure code runs as expected. 

![Testing_part_1](https://github.com/lauraz-15/walk-active/blob/main/assets/readme_images/testing_part_!.png)
![Testing_part_2](https://github.com/lauraz-15/walk-active/blob/main/assets/readme_images/testing_part_2.png)

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
[Screen Recroder](https://chrome.google.com/webstore/detail/screen-recorder/hniebljpgcogalllopnjokppmgbhaden?hl=en) extension was used to record the screen and ezgif.com was used to cut the screen area and convert it into gif file.

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

### Credits

Database set up and connection with Google sheets was inspired by Lovesandwiches project.
The code for validate_user_entry(values) function was taken from Lovesandwiched walkthrough project.