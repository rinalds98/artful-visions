Savory Junction
=

Introduction
=

Savory Junction is a restaurant website with a fully functioning booking system. Users accessing this website will be able to reserve a table at a date and time that is suitable for them. It also informs the user if the restaurant is full at the selected time and date or if they have already reserved a table at that specific time. Users can also leave a review about their experience at the restaurant and give it a star rating.

The website can be viewed here: [Savory Junction](https://savory-junction.herokuapp.com/ "Savory Junction").

# Table of contents
- [User Experience](#userexperience)
- [Agile Development](#agile)
- [Features](#features)
- [Future Ideas / Development](#future)
- [Testing](#testing)
- [Deployment](#deployment)
- [Technologies Used](#technologies)
- [Credits](#credits)

<div id='userexperience'/>

User Experience
=

## **User Stories**
- ## **As a website owner I want that:**

    1. The website provides an easy and friendly experience when reserving a table. (Booking System)
    2. The website alerts the user when they complete an action ie. register/reserve/update/delete.
    3. The website allows the user to have an idea of what cuisine is available and to see previous customer reviews. (Review System)
------

- ## **As a website user I want:**
    1. To easily understand how to navigate the website (Site Pagination).
    2. Confident that the reservation system works (Booking System and Manage Bookings).
    3. Any actions that the user does gets displayed as alerts.
 ------

- ## **As a returning website user I want:**
    1. To be able to view/update my reservation. (manage bookings)
    2. To be able to reserve another table. (Booking System)
    3. To view the menu.


# 1. Strategy

- The main purpose of this website is so users can reserve a table at their desired date and time.
- Each user creates an account so they can create/read/update/delete their reservation.

# 2. Scope
- After a few design choices. A simple 3-page layout for users logged in and 2-page layout for users logged out (excluding the log-in/log-out pages) was chosen for ease of navigation.
- Using UX design, mobile responsiveness, and simple color profile.

# 3. Structure
- The user would be greeted with a restaurant image and a call to action button.
- To create a reservation the user would be prompted to log in or register.
- The reservation page would a have simple form design for the user to select a desired date and time.
- The user would be alerted if the booking was successful or that the reservation failed due to the restaurant being full.
- The user could then see their current reservations on the "manage bookings" page.
- In the manage bookings page, the user would be allowed to update their reservation which would include either updating the time 
  of the reservation or deleting the reservation.

# 4. Skeleton
## **Design**
- The initial design was made using Wireframes.

    - ![Wireframe](/static/images/wireframe.png)

- The initial idea of how the system was going to work was sketched on Lucid Charts:

    - ![Lucid Charts](/static/images/lucid-chart.png)

# 5. Surface
 - ## **Color**
   - The basic color scheme would be dominated by white. With navy/black nav and footer bars. And the images would have a more 
     dominant orange color.
   - Buttons to log in/register and make a reservation would be green.
   - To update/delete a reservation they would be red.
        - ![Color Scheme](/static/images/color.png)

<div id='agile'/>

Agile Development
=

## Introduction
This project was developed using agile development by adding small features during the length of the project. All user stories were assigned labels (Must Have, Should Have, Could Have). They were assigned based on the importance of the project and its functionality.

The KanBan board can be accessed from the following link -
[Kan Ban Board](https://github.com/users/rinalds98/projects/3/views/1 "Kan Ban Board")


A Kanban board was created using GitHub projects where all the user stories were shown in a card format.
- ![Kan Ban Board](/static/images/kanban.png)

 ## **Reasons some User Stories currently not implemented**
- The user story related to date availability was not fully implemented. While users can choose a date and time. They won't be informed that it's booked until they click the submit button. Although this would enhance the user experience, I decided it would be a lower priority (Could Have Label) as the main focus was on website functionality.

- The user story related to Dietary information was not added due to it being a lower priority and deemed not necessary for creating a reservation at the restaurant. 

Due to the time constraints and scope of the project. I would not have enough time to develop and test these new functions before the project deadline.


<div id='features'/>

Features
=

The website Savory Junction is a simple website that allows the user to create a reservation for the restaurant. Even though it looks very simple on the outside there are a lot of things working in the background so the user can have a pleasant experience while using the website.

- ## **Home Page**
    - When the user first access the website he is greeted with a simple homepage design with a background image of the restaurant. The name of the restaurant and a call to action to make a reservation. There is also a Nav bar to access different parts of the website such as creating a booking, Managing a booking, and Log-In/Log-Out/Register buttons depending on the user's status.
        - ![Homepage](/static/images/homepage.png)

- ## **Review Section**
    - The review section first shows customer reviews in a card style using Bootstrap. The user can add a comment and a star rating. The section where the review is created can only be accessed when logged in.
        - ![Review Section](/static/images/review.png)

- ## **Create a Reservation**
    - The Create a Booking section has a very simplistic design. It allows the user to select a date with a date picker and then the specific time that they wish to reserve.
        - ![create Reservations](/static/images/createreservation.png)

- ## **Manage Reservations**
    - After the user has created a booking. They can go to manage their reservations in the manage booking section. It shows the time and date that the user selected. They can also update the reservation. If no bookings have been found it will display a text saying 'no bookings found' 
        -![Manage Reservations](/static/images/manage.png)

- ## **Update Reservations**
    - If the user wishes to update their reservation they have a choice of updating the date and time but also deleting the reservation in case they wish to cancel.
        - ![Update Reservations](/static/images/update.png)

- ## **Validate Selection**
    - There is a built-in modal from Bootstrap that is a failsafe in case the user clicks the delete button by accident. It allows the user to confirm whether to delete the reservation or keep it.
        - ![Confirmation](/static/images/modal.png)

- ## **Footer**
    - A very simple footer was chosen with social media icons that link to the business's social accounts. they use 'target=_blank' so if the user clicks they won't navigate anyway from the website.
        - ![Confirmation](/static/images/footer.png)

<div id='future'/>

Future Development
=

## **Further Development**
- Dietary information implementation into the reservation.
- Shows available dates and not just a date to choose.
- Users can update and delete their reviews.
- Users can delete their accounts.
- Users would be able to select how many guests they want to bring and in turn, get a table that can seat all the guests.


 ## **Reasons they are not currently not implemented**
- Due to the time constraints and scope of the project. I would not have enough time to develop and test these new functions before the project deadline.


<div id='testing'/>

Testing
=

## **Solved Bugs**
- The Star rating system when selecting 2 stars would light up stars(2, 3, 4, 5) but it should only light up stars (1, 2) It was fixed by using display flex and reversing the order. The checkbox(Stars) values also had to be changed so they would correspond to the correct star.
- Update reservation wasn't updating properly and even though 10 tables would create an 11th reservation for a reserved table.

## **Unfixed Bugs**
- once a user selects a rating if they click away or decide they want to write a review the star rating selection disappears.
This is purely aesthetical as the rating the user selected will still be posted to the database.
The way to fix this would be to use javascript for the star rating system rather than just CSS.
- When a user is selecting a date. They can select a date that is in the past.

## **Validator Testing**

- **Python Validation**
    - PEP8online.com was down during testing so I installed pycodestyle in VSCode. Then I searched for Linter and selected 'pycodestyle'. This showed if I had any errors which as of deployment is error-free.
    - The 2 problems that are shown are not related to the project itself. They are from the Code Institute template.

    ![Linter Check](/static/images/temperror.png)

    - All code that was written by me in the booking app is pep8 complaint. which are:
        - admin.py
        - forms.py
        - models.py
        - urls.py
        - views.py
    - While checking if everything was pep8 compliant I noticed the Django-provided code inside of the settings.py file was not. I was not able to fix this as the links in the 'AUTH_PASSWORD_VALIDATORS' were too long.
        - ![settings.py](/static/images/settings.png)
    
    - The same situation was also for my env.py file. The links were too long.
        - ![env.py](/static/images/env.png)


- **HTML Validator**
    - I ran my website through  [HTML Validator](https://validator.w3.org/ "HTML Validator") and received no errors.
    ![HTML Check](/static/images/htmlvalidator.png)

- **CSS Validator**
    - I ran my website through  [CSS Validator](https://jigsaw.w3.org/css-validator/ "CSS Validator") and received no errors.
    ![CSS Check](/static/images/cssvalidator.png)

- **JS Validator**
    - I ran my website through  [JS Validator](https://jshint.com/ "JS Validator") and received no errors only undefined $ for jquery. An issue with bootstrap being undefined but because I am using bootstrap javascript I assume that's the reason why.
    ![jS Check](/static/images/jshintvalidator.png)

- **Console Errors**
    - There was no console errors found.
    ![Console Check](/static/images/errorfree.png)

- **Lighthouse Check**
    - This was my Lighthouse check
    ![lighthouse Check](/static/images/lighthouse.png)


## **Manual Testing**
The Following was tested manually and passed:
- **Navbar**
    - Savory Junction Logo brings the user back to the homepage.
    - User logged out:
        - Home link - works as intended bringing the user back to the home page.
        - Create a booking - brings the user to the create a booking page.
        - Log-In/Register - brings the user to the respective pages.
        - Does not show 'Manage Bookings' or 'Log-Out' nav links
    - User Logged In:
        - Home link - works as intended bringing the user back to the home page.
        - Create a booking - brings the user to the create a booking page.
        - Manage Bookings - brings the user to the manage bookings page.
        - Log-Out - brings the user to the log-Out page.
        - Does not show 'Log-In' or 'Register' nav links.

- **Homepage**
    - Call to action button
        - 'Make a reservation' button works as intended - brings the user to the Create a Booking page.
    - If the user is not logged in.
        - The review section of the home page will only show reviews posted. If the user wants to leave a review they will need to log in.
        - The log-In button works as intended, bringing the user to the Log-In page.

- **Review Section**
    - If the user is logged in there will be a star rating system and text area for a user to leave a review.
    - Trying to post a review without selecting a star and inputting text in the text area. The user will get a "please select one of the options" and "please fill out this field".
    - If the user has already posted a review they will get an alert that states they have already made a review.

- **Create a Reservation**
    - User Logged Out:
        - They will not be able to create a reservation. They will be asked to Log-In/Register.
        - Log-In/Register buttons work as intended bringing the user to the intended destination.
    - User Logged In:
        - The user can select a time to reserve a booking.
        - Date picker works as intended showing a calendar to choose a date.
        - The reserve button works as intended submitting the user's reservation details to the database.
    - Reservations:
        - If all tables are booked for a specific date and time the user will get an alert stating that all tables are booked.
        - If the user has already booked that specific time. They will receive an alert stating they have already booked a table at this time.
        - If a table is available and the user hasn't already booked the specific time the user will get an alert 'booking made successfully'.

- **manage Bookings**
    - User Logged Out:
        - They will not be able to access 'manage bookings'.
    - User Logged In:
        - The update button works as intended which will bring them to the update page.

- **Update Bookings**
    - The user can select a time to update a booking.
    - Date picker works as intended showing a calendar to choose a date.
    - The reserve button works as intended submitting the user's updated reservation details to the database.
    - Delete button - when clicked brings up a modal that asks for confirmation to delete a reservation.

    - Modal Buttons
        - Keep Button - Cancels the delete request.
        - Delete Button - deletes the user's reservation.

- **Log-In/Log-Out/Register Pages**
- The log-In/Log-Out/Register sections are managed by OAuth Library.

    - **Register page**
        - If a username has already been used the user will get an error stating that a user already exists with that name.
        - The user is required to have a username and password.
        - The password confirmation has to match.
        - The password can't be simple or a common name.
        - The sign-up button registers the user's account and they are logged in.
        - The sign-in link brings the user to the Log-In page.
    
    - **Log-In Page**
        - The user is required to have a username and password.
        - The password has to be correct.
        - The sign-up link brings the user to the register page.
        - The sign-in button logs the user on.
    
    - **Log Out Page**
        - Sign out page works as intended logging the user out of their account.

- **Footer**
    - All social media icons work as intended bringing the user to the correct social media website.
    - each social media link has a 'target="_blank"' so it opens a new tab instead of navigating away from the website.

- **Alerts**
    - Alerts have been programmed to disappear after 3 seconds which is True.

<div id='deployment'/>

Deployment
=

**The website was deployed using Code Institute's GitHub template on Heroku. The steps to deploy are as follows:**
- Create a new Heroku app.
- In the settings, enter the following Config Vars:
    - PORT: 8000
    - SECRET_KEY: (Enter your secret key)
    - DATABASE_URL: (Enter the database URL from ElephantSQL)
    - CLOUNDINARY_URL: (Enter Cloudinary API URL)
- Link the Heroku app to the repository.
- Click on Deploy. 


The live link can be found here [Savory Junction](https://savory-junction.herokuapp.com/ "Savory Junction").

<div id='technologies'/>

Technologies Used
=

- ## Languages
    - Html
    - CSS
    - Javascript
    - Python

- ## Frameworks and Tools Used
    - Django
    - Bootstrap
    - ElephantSQL
    - Cloudinary
    - Github
    - Heroku
    - Balsamiq Wireframes
    - Python Library "ruff" - Python Linter
    - Python Library "Black" - Format code to PEP8 compliancy
    - OAuth - Account Management


<div id='credits'/>

Credits
=


## **Content**
