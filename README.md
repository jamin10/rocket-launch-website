# Rocket Launch Tracker

This webapp allows users to look at past and upcoming rocket launches and bookmark those which they are interested in. 

## Deployment

A Dockerfile has been included to run the webapp in a container. Use the following commands while inside the root directory:

1. `docker build -t rocket-launch-website`
2. `docker run -p 5000:5000 -d rocket-launch-website`

Go to 'localhost:5000' in web browser.

## Usage 

* Register for an account with username and password
* Use navbar to view different pages 
* Use the filter to retrieve your desired information 
* Click `Bookmark` button to save a rocket launch to your account 
* Logout to switch accounts 

## API

Data for the launches are taken from The Space Devs API.

https://thespacedevs.com/llapi.

## Future Improvements

* Add a homepage with space news
* Use PostgreSQL for database
* Run database in separate Docker container 
* Add a countdown to launch
* General styling improvements 

