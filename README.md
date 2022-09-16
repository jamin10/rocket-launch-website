# Rocket Launch Tracker

This webapp allows users to read the latest space news, look at past and upcoming rocket launches, and bookmark those which they are interested in.

## Deployment

A Dockerfile has been included to run the webapp in a container. Use the following commands while inside the root directory:

1. `docker build -t rocket-launch-website`
2. `docker run -p 5000:5000 -d rocket-launch-website`

Go to 'localhost:5000' in web browser.

## Usage 

* Register for an account with username and password
* Use navbar to view different pages 
* Homepage shows recent space news with links to articles
* View past and upcoming rocket launches
    - Use the filter to retrieve your desired information 
    - Click `Bookmark` button to save a rocket launch to your account 
* Logout to switch accounts 

## API

Data for the launches and news are taken from The Space Devs APIs.

https://thespacedevs.com/llapi
https://thespacedevs.com/snapi

## Files

main.py
* Executable to run programme

\_\_init\_\_.py
* Initialises app 
* Create database if doesn't already exist

auth.py
* Routes which allow users to login, logout, register
* Handles some backend security checks 

views.py
* Routes to pages of the website 
* Calls to API to pass information to frontend
* Routes for buttons to bookmark launches

models.py
* Sets up database models 
* User has a one-to-many relationship with Launch

helpers.py
* Abstracts away useful functions 

templates/
* Contains HTML templates for the webpages
* Uses Jinja and JavaScript functions

index.js
* Contains functions for buttons to bookmark and delete

## Future Improvements

* Use PostgreSQL for database
* Run database in separate Docker container 
* Add a countdown to launch
* General styling improvements 

