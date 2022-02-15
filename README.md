# Restaurant Management App
This app was built to give users the ability to create bookings, view the total number of bookings and calculate the number of staff required per day for a restaurant.  

This app was made as the fulfillment of the Milestone Project 3 for the Full-Stack Software Development Course provided by Code Institute. It was made using Python and deployed on Heroku using Code Institue's mock terminal.

The live website can be found [here](https://restaurant-budget.herokuapp.com/)

![Responsive Website](./assets/images/responsive_test.png)

## Table of Contents

- [How to Use](#How-to-Use)
- [Goals](#Goals)
    - [User Goals](#User-Goals)
    - [Project Flow and Processes](#Project-Flow-and-Processes)
    - [Limitations](#Limitations)
- [Features](#Features)
    - [Future Features](#Future-Features-to-Implement)
- [Technologies](#Technologies)
    - [Languages](#Languages)
    - [Tools](#Tools)
- [Testing](#Testing)
    - [Overview](#Overview)
    - [Validator Testing](#Validator-Testing)
    - [Issues/Bugs Resolved During Testing](#Issues/Bugs-Resolved-During-Testing)
    - [Testing User Goals](#Testing-User-Goals)
- [Deployment](#Deployment)
- [Credits](#Credits)
- [Acknowledgments](#Acknowledgments)

****

## How to Use

The Restaurant Management App is designed to improve efficiency, reduce errors and be an easy way for all restaurant managers to create bookings, view bookings and the minimum number of staff needed for each working day.

The user has three options upon opening the app:

1. Enter a new booking
2. View total number of bookings
3. Caluclate staff numbers required for the upcoming week

The user selects their desired option and follows the on screen instructions. Dependant on their choice they will be shown an output with their desired data.

The app is designed for all restaurant bookings to be made through the app throughout the previous week, then towards the end of the week the number of staff can be calculated so a work schedule can be produced. 

***

## Goals

#### User Goals

- As a user I want to be able:

    - To make a booking for a specific day inputting the number of guests required for the booking.
    - To save this booking and it to add to the total number of people booked in that day. 
    - To view the total number of people booked in on any given day in the week.
    - To be able to see how many staff are required for the number of people booked.
    - To be able to reset the bookings and start again each week.

### Project Flow and Processes

- An initial flow chart was sketched out at conception of this project.
- This was updated as the project evolved and a final flow chart was made on Lucidchart.
- Each input was validated using a try/except statement, however this is not shown on the flow chart

![Flow Chart](/assets/images/flowchart.png)

### Limitations

- As the app is run using Code Institue's Mock Terminal it doesn't offer a particularly user friendly interface. This could be improved by adapting the terminal or creating original HTML/CSS code for the app, turing it into a Full Stack Project.  

***

## Features

### Existing Features

#### Google Sheets
- The Google Sheet was set up to host all the historical data the restaurant had been using up until this point.
- The app will take data from this sheet and use it, in conjunction with new input data, to calculate the outputs (number of staff needed etc.)
- All data used within this app; input data, data from calculations and output data; will be stored in this Google Sheet. 
- The Google Sheet consists of four worksheets representing bookings, walk-ins, takings and number of staff on shift. Each worksheet has seven columns, representing the days of the week, and each row represents a new week. 
- The bookings worksheet has an extra row, with all 0 as this is the starting point for each weeek where no bookings have been made yet. 
![Google Sheets](/assets/images/google_sheets.png)

#### Main Menu
- The main menu welcomes the user to the app and asks them to select a choice of three options:
    - Enter a new booking
    - View the total number of bookings
    - Calculate staff numbers required for the upcoming week
- The user must answer using the numbers 1 to 3. If they input data that is not a number the error 
> "Invalid data: invalid literal for int() with base 10" 

is raised.
- If the user inputs a number that is not 1 to 3 they error
> "Invalid data: Input must be 1, 2 or 3. Please try again" 

is raised. 
- The user is then asked to select again in both instances.
![Main Menu Invalid Data](/assets/images/main_menu_invalid.png)

#### Make Booking
- Upon selecting option 1 the user is prompted to input a day of the week
- Again an error will be raised if the data is invalid.
- Once a valid input have been made the user will have to input the table size. This is limited between 1 and 10 (inclusive) to limit large tables without pre-ordering/deposits etc. This data is also validated
- Successful input of the day and party size will result in the terminal printing out a dictionary summarising the booking and a message asking if you wish to save your booking. 
- Should the user selects "Y" the user will be told the booking is saved. The Google Sheet will be updated to add the party size to the last row and relevant column in the bookings worksheet. 
- If the user selects "N" no further action to the dictionary will be taken. Both choices are followed by the return the menu section, discussed later.  

![Booking section](/assets/images/booking_section.png)

#### View Bookings
- If the user selects option 2, a total of all bookings per day is displayed.
- This is displayed as a dictionary which has had it's order fixed to follow the order the days of the week fall.
- If the user selects this option first or early on in their use it will display all 0 or mainly 0. This is because no or few bookings have been made and as more bookings are made this fill up. 

![View Bookings](/assets/images/view_bookings.png)

#### Calculate Staff Needed
- If option 3 is chosen the user is met with a message explaining that calculating the number of staff resets the bookings for the following week and asks them if they have completed all their bookings.
- Again the input for this answer is validated with errors raised in the event of invalid data.
- If "N" is selected the user is taken back to the main menu and prompted to complete their bookings.
- If "Y" is selected the calculating staff function is run. 
- This function performs the following steps in order:
    - Calculate the average number of walk-ins over the last 10 weeks 
    - Iterates over the two lists adding the values together to create a "Total number of covers per day" list
    - Multiplies the total covers list by 15 for Monday to Thursday and by 25 for Friday to Sunday to calculate the predicted takings in pounds. 
    - Divides the predicted takings list by 400 to calculate the minimum number of staff required to work per day. 
    - If the number is only 1, an extra staff member is added.
    - If the day is Friday to Sunday and extra staff member is added
    - This list is then used along with the days of the week to create a dictionary and printed to the terminal.
    
![Calculate Staff](/assets/images/calculate_staff.png)

#### Return to Main Menu
- All choices are followed by an option to return to the main menu. 
- If "Y" is selected it will return the user to the main menu where they can select again from the three initial options.
- If "N" is selected the user is thanked for using the app and it ends. 

### Future Features to Implement
- The ability to input a time of booking, not just day and number of people, would allow the user to have greater knowledge on when tables are booked.
- In addition each day could be split into three "services", breakfast, lunch and dinner. The app could then be updated to calculate staff required for each service for each day, providing a more realistic overview of how a restaurant needs to schedule it's staff. 
- Another feature to be added in the future is the ability to make bookings further in the future than the current week. This could be done by using a date function, or a week commencing function.
- Tieing into this the ability to view historical data/bookings/staff numbers without going to the Google Sheets would be useful to improve budgetting ability.
- The four features above, are one step in the road into developing this app into a full business management/CRM style app. This is where I envision this app developing in the future. 

***

## Technologies

### Languages
- The project was written using Python 3.8.11
-  The following modules and APIs were installed to improve the output and functionality:
    - Math - Used for the ceil() function to round numbers up to the nearest integer
    - Statistics - Used for the fmean() function to calculate the mean average and reduce the amount of code needed
    - Gspread - API for Google Sheets used to get and update the worksheet 
    - Google Auth - Authenticates Google's APIs and takes the credentials from the Google Sheets 

### Tools    
- Gitpod was used as an online IDE
- Github was used as the repository for the source code
- Herkou was used as the platform to run the deployed app
- Google Sheets was used to store the data and where the initial "historical data" was held
- Code Institute's Python Essentials Template was used to view the app in a mock terminal
- PEP8 checker was used to check the Python code for errors 

***

## Testing

### Overview

Testing will be performed on the functionality of the app. The ease of use and clarity will also be reviewed to ensure the back-end code integrates nicely with the front-end design. 

Testing will look for the following:

- The interaction and statements printed to the terminal are clear and easy to follow.
- All inputs are checked and validated to ensure the user does not input invalid data type. Errors will be raised and an opportunity to try again will be allowed following invalid data entry.
- No unexpected errors occur once deployed to Herkou and all errors raised are due to user input error.
- The user is given the option to return to the main menu upon finishing their action for ease of use/
- All bookings made by the user are saved to the Google Sheet and then can be pulled up prior to calculating staff numbers.

### Validator Testing

- Python
    - The official PEP8 online syntax checker came back with no issues. 

    ![PEP8 online checker](assets/images/pep8_checker.png) 


### Issues/Bugs resolved during testing 

- Upon deployment the dictionary showing the current weeks bookings that was printed to the terminal was difficult to read and spread over across two lines. This was resolved by installing the pprint() function to make it clearer in the terminal with each new key:value pairing print on a new line.

- The fix above then created a new bug. In Python 3.8 + the print() function orders dictionaries in order of creation of key:value pairs. However, pprint() orders them alphabectially by key. This was solved by adding "sort_dicts=False" inside each pprint function.

- If the user selected "Y" to return to the main menu within function "restart()" and then selected "N" to end the app once "restart()" is run a second time, two identical print statements were returned in the format:
     > "Thank you for using the restaurant management app.
Thank you for using the restaurant management app"

    This was fixed by creating a new function "main_menu()" which only runs the "start()" function if the variable is True.

- I originally had the inputs accepting those starting both with and without a capital letter (e.g. Monday or monday). This made for a large number of if statements within my try statements. I didn't wish to remove the ability to use lower case as it takes away from the user friendliness of the app. To fix this I added the .capitalize() method to the end of all my input() functions, automatically Capitalizing the input, making them valid (provided the input is of the correct type).

### Testing User Goals

- The user goals listed in the User Goal section were tested to ensure the project outcomes were met and the app has good real world use.  

1. To make a booking for a specific day inputting the number of guests required for the booking.
    - Upon running the app select option 1 which allows the user to make a booking Monday - Sunday of up to 10 people
2. To save this booking and it to add to the total number of people booked in that day. 
    - Within option 1, the user has the option to save their booking, which adds the booking to the last row in the bookings worksheet
3. To view the total number of people booked in on any given day in the week.
    - Select option 2 in the main menu and a dictionary in the form {day: number of people booked} will be printed to the terminal for all days of the week
4. To be able to see how many staff are required for the number of people booked.
    - After running the app, select option 3 in the main menu. This choice will calculate the minimum number of staff required per day and print it in another dictionary in the form {day: number of staff needed}.
5. To be able to reset the bookings and start again each week.
    - Option 3 automatically resets the bookings back to 0 whilst calculating the number of staff needed. It gives the user the choice if they wish to proceed, incase it was pressed accidentally.
    - The user can then restart the app with a new week and input new bookings

***

## Deployment 

The project is hosted by Heroku using Code Institute's Python Essentials Mock Terminal:

### Deploy to Heroku

Please deploy the app to Heroku using the following steps:

1. Log into Heroku and click the 'New' button and then "Create new app" from the drop down list
2. Name your app (it must be unique) and select the region you are based in
3. Select settings and scroll down to the config vars section
4. Within config vars enter CREDS into the key field and the contents of your creds.json file into the value field. This allows Herkou to have access to your Google Sheets.
5. Add another config var of PORT (key) 8000 (value) to ensure the mock terminal works.
6. Select the buildpack button and add two buildpacks of Python and NodeJS in that order
7. In the connect to Github section, add the repository name to link the Github.
8. Press deploy to deploy the app to Heroku, you can also opt in to "Enable Automatic Deploys" which updates the Heroku everytime a new change is pushed to Github.

### Fork the GitHub

If you wish to view or make changes without affecting the original repository you can 'fork the repository'. This creates a copy to your GitHub and can be done using the following steps:

1. Log in to Github and locate the [Restaurant Budget Repository](https://github.com/tdawes93/restaurant-budget)
2. At the top right of the repository underneath the notification icon is the 'fork' button
3. Click this button and you should now have a copy of the repository in your Github account

### Make a local clone

1. Log in to Github and locate the [Restaurant Budget Repository](https://github.com/tdawes93/restaurant-budget)
2. At the top of the repository next to the 'Gitpod' button click the dropdown named 'Code'
3. To clone the repository using HTTPS, make sure HTTPS is selected and copy the link
4. Open the Git Bash
5. Change the working directory to the location you wish the clone to be made
6. Type 'git clone' and paste the copied URL
7. Press 'Enter' and your local clone will be created

### Using repository with own historical data

Please be aware that if you wish to use this repository for your own business or with your own historical data, you must use the following steps in addition to above:

1. Create a Google Sheets using the same format as shown in the features section. It must have four worksheets and seven columns, all with the same names/labels as shown 
2. In Google Cloud Platform, create a project and link the Google Sheets using the Google Drive and Google Sheets APIs
3. Save the downloaded "credentials file" and upload it into your Gitpod in a cred.json file (this is the contents you need in the deployment section)
4. You can now continue to deployment. 

***

## Credits
- Inspiration
    - The idea for this app along with suggested future updates was borne from countless weeks having to estimate takings and staff numbers required whilst managing pubs

- Code
    - The update_worksheet function was take from Code Institute's Love Sandwiches Mini Project


***

## Acknowledgments

I'd like to thank my mentor Spencer Bariball for his support and feedback throughout the project. I'd also like to thank the group of friends and family I had test and give feedback on the site on their various mobiles and laptops.