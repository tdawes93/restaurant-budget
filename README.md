# Restaurant Management App
This website was built to give users the ability to create bookings, view the total number of bookings and calculate the number of staff required per day for a restaurant.  

This app was made as the fulfillment of the Milestone Project 3 for the Full-Stack Software Development Course provided by Code Institute. It was made using Python and deployed on Heroku using Code Institue's mock terminal.

The live website can be found [here](https://restaurant-budget.herokuapp.com/)

![Responsive Website](./assets/images/responsive_test.png)

## Table of Contents

- [How to Use](#How-to-Use)
- [Goals](#Goals)
    - [User Goals](#User-Goals)
    - [Site Owner Goals](#Site-Owner-Goals)
    - [Differences in finished site](#Differences-in-finished-site-to-initial-design)
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
    - [Testing User Stories](#Testing-User-Stories)
- [Deployment](#Deployment)
- [Credits](#Credits)
- [Acknowledgments](#Acknowledgments)

****

## UX Design 

### User Stories

#### First Time Visitor Expectations

- As a first-time visitor I want:

    - To understand the purpose of the site and learn how to play the game.
    - To be able to know how to start the quiz and navigate the site immediately.
    - To find the game interesting and challenging.
    - To see my score when the quiz is finished.
    - To be able to play the quiz on all devices.

#### Returning/frequent Visitor Expectations

- As a returning/frequent visitor I want:

    - To continue to enjoy the quiz even after multiple attempts.
    - To find the saved League Table and try and beat the high scores.
    - To share my high score on social media.

### Structure

- A navigation bar will be on the homepage with links to each section/modal. Navbar titles will be Kick-off, Rules and League-Table. This fulfills the user stories:
    - > "I want to understand the purpose of the site and learn how to play the game."
    - > "To be able to know how to start the quiz and navigate the site immediately."
- The homepage will provide a basic hook line drawing the user in and explaining what to do. This fulfills the user story:
    - >"I want to understand the purpose of the site."
- The use of CSS and media queries will make the website responsive. The initial design will be for mobile devices and the responsive design will ensure the layout changes as the screen size increases. This fulfills the user story:
    - >"I want to be able to play the quiz on all devices"
- The quiz section will contain a question container and then a results container when the quiz is finished. This will display the score to the user. This will fulfill the user story:
    - >" To see my score when the quiz is finished."
- The results modal will contain a short form where the user can input their name and save it to the league table. The league table modal will display the top 20 high scores in order from highest to lowest. This will fulfill the user stories: 
    - >"To see my score when the quiz is finished."
    - >"To be able to play the quiz on all devices."
    - >"To find the saved League Table and try and beat the high scores."
- The rules modal will contain a list of the rules and methods to play this quiz. This fulfills user story:
    - >"To be able to know how to start the quiz and navigate the site immediately."

### Design

#### Colour Scheme

- The three main colours used were Red #EF0001, White #FFFFFF and Oxford Blue #172030. These colours were taken from the Arsenal FC logo to ensure they are official Arsenal FC colours. This allows the site to be instantly identifiable by football fans. 

- The kick-off button is coloured in Metallic Sunburst #9D8349 and the background of the page is coloured in Cultured #F1F2F3. Both these colours are taken from the official Arsenal FC website and stick with the main theme.

![Colour Scheme](/assets/images/readme-images/coolers.PNG)

#### Typography

- Source Sans Pro is used throughout the site. It is a sharp, clear and crisp font making it easy to read. It is similar to FF Meta which is the font used on the official Arsenal FC site.

- The site uses uppercase for titles and buttons and capitalisation for all other text. This enables readability and allows the buttons to be easily identified.  

- The font has a sans-serif backup.

#### Imagery

- The images were selected as they show famous moments in Arsenal's history. They were chosen to create excitement whilst being a trip down memory lane.

- The images have been resized to be responsive.

### Wireframes/Skeleton

##### Home Page
![Home Page Wireframe](/assets/images/wireframes/homepage.PNG)

##### Quiz Container
![Quiz Container Wireframe](/assets/images/wireframes/quiz-container.PNG)

##### Results Modal
![Results Modal Wireframe](/assets/images/wireframes/results-modal.PNG)

##### Rules Modal
![Rules Modal Wireframe](/assets/images/wireframes/rules-modal.PNG)

##### League Table Modal
![League Table Modal Wireframe](/assets/images/wireframes/league-table-modal.PNG)

### Differences in finished site to initial design 
1. The "Kick-off" button is now placed in the centre of the homepage and coloured in gold. It was originally designed to be on the nav bar on the top left. However, after user feedback during the testing stage found that many users were unsure how to start the game, it was moved to be more clear and concise. 

2. The initial site was going to include a share now button to enable the user to share their score on social media and encourage others to play the quiz. This feature was not implemented as the social media accounts do not exist and to keep the quiz simple to use. 


### Limitations

- The functionality of the quiz is made using JavaScript (JS) meaning the quiz built in front-end development. If the user wanted to, they would be able to access the JS code and see the correct answers. In the future, the questions and programming code could be written in a back-end language to avoid this issue. 


***

## Features

### Existing Features

#### Home Page
- Header and navigation bar
    - Located at the top of the homepage it allows the user to navigate between the rules and the league table modals.
    - The design is styled on the official Arsenal FC website using the same colouring and container/box styles.
    - The JavaScript will bring up the rules and league table modals when the corresponding button is clicked.

![Header and Navigation bar](/assets/images/readme-images/navigation-bar.PNG)
- Hook line and Kick-off button
    - A short hook line is located just underneath the navbar, it allows the users to know what the website is about and what their first course of action should be.
    - The Kick-off button is located centrally on the page and is a bright contrasting colour making it easy to find and obvious to the new user.
    - The Kick-off button initiates the quiz, using JS when clicked, and pulls up the first question.

![Hook line and Kick-off button](/assets/images/readme-images/hook-line-kickoff-button.PNG)
- Footer
    - The footer section contains my name and a link to my GitHub page so users know who the author is and where they can access other sites made by me. 
    - It also matches the header creating symmetry and improving the style of the site.
    
![Footer](/assets/images/readme-images/footer.PNG)
#### Quiz Container
The quiz container is split into two sections the question section and the answers section.
- Question Section
    - The question section is a famous arsenal image with the question overlaid on top.
    - The question is in 'bubble style' writing with a black border to allow the users to read the question.
    - Above the image is a question counter so the user knows how many questions they have answered.
    - JavaScript takes the question property from the relevant object in the questions array and places it into the inner HTML, displaying the question.

![Question Section](/assets/images/readme-images/question-section.PNG)
- Answers Section
    - The answers section is made up of four potential answers inside buttons.
    - The answers are generated in the same way as the question, the JD takes the answers property from the relevant object in the questions array.
    - When the user selects their answer the correct answer will highlight the button in green. If the selected answer is wrong it will highlight in red, with the correct one in green.
    - This is performed using an event listener comparing the Id of the clicked answer with the correctAnswer value in the questions array.
    - The quiz then waits 1.5 seconds before moving on to the next question to allow the user to see if they answered correctly or not.

![Answers Section](/assets/images/readme-images/answers-box.PNG)

#### Results Section
- Score and result
    - The top part of the results section displays the score and the result category. The category gives a short humourous snippet that keeps the user engaged and motivates the user to try again.
    - A for loop is run to bring up the different result categories and funny caption.
    - The bottom half of the results section allows the user to input their username and save it to the league table.
    - The save button will not be activated until a username has been typed into the input.
    - Once the save button is clicked, the JavaScript will create an object from the score and name before adding it into the high socres array. This array is then ordered, spliced and stored in local storage.
    - There is also a small nav bar with Homepage, Rematch and League-table buttons. This navbar allows the user to replay the game or navigate away from the results without saving their score.

![Results Section](/assets/images/readme-images/results-section.PNG)
#### League Table Modal
- The league table modal contains a table displaying the top 20 scores and their respective "league" positions. This allows the user to see their score compared to other people around them.
- The JS uses the .map() method to create a new object with using HTML and the highscores array, this is then added to the inner html of the table.
- There is also a back button that takes the user back to the homepage.

![League Table Modal](/assets/images/readme-images/league-table-section.PNG)
#### Rules Modal
- The rules modal contains a list of rules and methods on how to play the quiz.
- It is styled the same as the league-table modal and also includes the back button.

![Rules Modal](/assets/images/readme-images/rules-modal.PNG)

### Future Features to Implement
- Questions could be randomised
- Greater choice of questions that changes the quiz each time it loads which allows frequent users to have a better experience
- Add a button allowing the user to select their favourite team which then brings up questions for each team improving user demand. 

***

## Technologies

- Languages
    - The project was written using Python 3.8.11
    -  The following modules and APIs were installed to improve the output and functionality:
        - Math - Used for the ceil() function to round numbers up to the nearest integer
        - Statistics - Used for the fmean() function to calculate the mean average and reduce the amount of code needed
        - Gspread - API for Google Sheets used to get and update the worksheet 
        - Google Auth - Authenticates Google's APIs and takes the credentials from the Google Sheets 

- Tools    
    - Gitpod was used as an online IDE
    - Github was used as the repository for the source code
    - Herkou was used as the platform to run the deployed app
    - Google Sheets was used to store the data and where the initial "historical data" was held
    - Code Institute's Python Essentials Template was used to view the app in a mock terminal
    - PEP8 checker was used to check the Python code for errors 

***

## Testing

### Overview

Testing will be performed on the layout, structure and styling of the website. Tests were also performed on the functionality of the site. To do this dev-tools (and its other browser counterparts) will be used to view the site on different browsers and different device sizes.

In addition, the deployed site will be tested directly on different devices. The devices used were:
- Laptop with 1920 x 1080px screen
- Google Pixel 3a phone
- Huawei P20
- One plus 8 Pro

Testing will look for the following:

- All elements will remain where designed for all screen widths, with no overlapping or misalignment.
- All buttons will direct correctly with external links opening in a new browser tab.
- Correct answers will be displayed in green, incorrect answers in red.
- The score is calculated correctly and resets when the user restarts the quiz either through the rematch button or kick-off button.
- The form will not allow a blank username to be saved and all saved scores are placed in the local storage.
- The saved score is added to the high scores array and stored in local storage.
- Media shows clearly and is not distorted
- HTML and CSS will be validated using W3C and Jigsaw
- All pages will have a Lighthouse report generated to test for
    - Performance
    - Accessibility
    - Good Practices
    - SEO
- The User Stories from the UX Design section will also be tested

### Validator Testing

- Python
    - The official PEP8 online syntax checker came back with no issues. 

    ![PEP8 online checker](assets/images/pep8_checker.png) 


### Issues/Bugs resolved during testing 

- Upon deployment the dictionary showing the current weeks bookings that was printed to the terminal was difficult to read and spread over across two lines. 

- If the user selected "Y" to return to the main menu within function "restart()" and then selected "N" to end the app once "restart()" is run a second time, two identical print statements were returned in the format:
     > "Thank you for using the restaurant management app.
Thank you for using the restaurant management app"

    This was fixed by creating a new function "main_menu()" which only runs the "start()" function if the variable is True.

### Testing User Stories

The user stories explained in the UX Design section were tested to ensure they work as intended and are easy for the users to achieve. 

As a first-time visitor I want:

1. To understand the purpose of the site and learn how to play the game.
    - Upon entering the site the hook line explains the function of the site and tells you how to start the quiz.
    - The rules modal is easily found on the navbar, which brings up the set of rules and instructions on how to play.
2. To find the game interesting and challenging.
    - The questions are a range of difficulties and cover the entire history of the club.
    - The quiz is interactive and provides funny feedback to keep users engaged.
3. To see my score when the quiz is finished.
    - The user can save their score to the league table which then automatically loads.
    - The score is then saved into the site's local storage so can be accessed after reloading the page/closing and reopening it.
4. To be able to play the quiz on all devices.
    - Testing was performed across a variety of devices and browsers, all of which maintain design and function.

As a returning/frequent visitor I want:

1. To continue to enjoy the quiz even after multiple attempts.
    - The competitive edge of most users will allow the user to continue to enjoy the game
    - Within the features to implement section the quiz to have more questions added and include different teams to keep the quiz interesting and unique. 
2. To find the saved League Table and try and beat the high scores.
    - The league table button is easy to find and the league table loads automatically after saving the high score.
3. To share my high score on social media.
    - This user story has not been fulfilled but can be implemented in the future.


***

## Deployment 

### GitHub Pages

The project is hosted by GitHub and deployed using the following steps:

1. Log in to Github and locate the [Arsenal Quiz Repository](https://github.com/tdawes93/arsenal-quiz)
2. Click the settings button on the menu
3. Click 'Pages' on the list on the right or scroll down until you reach 'Github Pages' and click the link
4. Under 'Sources' select 'main' on the drop-down called 'None' and click save
5. The page will refresh with a link to the deployed site at the top, click this to go to the live website.

### Fork the GitHub

If you wish to view or make changes without affecting the original repository you can 'fork the repository'. This creates a copy to your GitHub and can be done using the following steps:

1. Log in to Github and locate the [Arsenal Quiz Repository](https://github.com/tdawes93/arsenal-quiz)
2. At the top right of the repository underneath the notification icon is the 'fork' button
3. Click this button and you should now have a copy of the repository in your Github account

### Make a local clone

1. Log in to Github and locate the [Arsenal Quiz Repository](https://github.com/tdawes93/arsenal-quiz)
2. At the top of the repository next to the 'Gitpod' button click the dropdown named 'Code'
3. To clone the repository using HTTPS, make sure HTTPS is selected and copy the link
4. Open the Git Bash
5. Change the working directory to the location you wish the clone to be made
6. Type 'git clone' and paste the copied URL
7. Press 'Enter' and your local clone will be created

***

## Credits

- Content
    - General inspiration for the layout and functionality of the quiz was taken from [Buzzfeed Quizzes](https://www.buzzfeed.com/uk/quizzes) and Paul Bowden's [MP2 project](https://github.com/PaulBowden673/Projects-MP-MP2-Quiz). 

- Code
    - The code for the saveScore function and the appendScore function was taken and adapted from James Q Quick's YouTube series [Build a Quiz App](https://www.youtube.com/channel/UC-T8W79DN6PBnzomelvqJYw).

    - The method and some of the code for the checkAnswer function were taken from David Walsh's article on [Event Delegation](https://davidwalsh.name/event-delegate).

    - The questions and answers were taken from [Fun Trivia Arsenal Section](https://www.funtrivia.com/en/Sports/Arsenal-7231.html).

- Media
    - All photos were either downloaded from [Unsplash](https://unsplash.com/) or [Pexels](https://www.pexels.com/).

***

## Acknowledgments

I'd like to thank my mentor Spencer Bariball for his support and feedback throughout the project. I'd also like to thank the group of friends and family I had test and give feedback on the site on their various mobiles and laptops.