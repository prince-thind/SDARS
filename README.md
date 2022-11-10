# school management system
This repository is the place for our draft codes. 

## assumtions before using
+ every username is unique and is handed over to the students before using this system
+ users are not supposed to reload the page as it will logout them
+ creation of new users is out of the scope for the current implementation.

## frontend

To start the frontend, follow the below steps:  
+ cd frontend
+ npm i
+ npm start

if you follow these correctly it should open a browser window with the project

+ note that you'd need nodeJS to be able to run this project

### Note for backend collaborators
+ apis specs are defined in the misc folder
+ assume all fields return strings, unless a type is specified in the conventional way in the api.
+ /login does not need to send an id field as usernames gotten from login screen act as unique identifier

## backend

backend instrcutions go here!