# Beer Diary
## A web-app to keep memories of all the beers you ever tasted and share it with friends!

#### Try [Beer Diary](https://beerdiary.herokuapp.com) yourself!
#### Video Demo: [watch](https://youtu.be/ocqnSbL1if4) on Youtube

  
#### 1. What is it?
  
Beer Diary is my final project for CS50: Introduction to Computer Science course.

Beer Diary is a web-application built on Django Framework.

Developed in 2021 by Anastasia Maryina (@nastiacooly).

#### 2. What can it do?
  
Beer Diary provides the following features to users:
  
- Registering account and logging in;
- Adding "memories" of beer to their Beer Diary;

"Memories" are like beer reviews where user can write his/hers impressions from a beer.
Memory consists of a beer name, beer image, beer type (for example, stout or lager), beer rating (from 1 to 5 stars) and additional optional comments.

- Users can also edit or delete their "memories";
- Seeing all their "memories" in a list for easy access;
- Searching their "memories" by a beer name;
- Filtering their "memories" by different characteristics such as beer type, filtered or unfiltered beer, light or dark beer and beer rating;
- Seeing their favourite "memories" (i.e., all the beers with 5-star rating);
- Searching other users by username and adding friends (also with help of suggestions for new friends based on mutual friendships);
- Seeing their profiles with account info, statistics (number of "memories" and etc.) and friends list and requests;
- Sending, accepting, rejecting and cancelation of friend requests and unfriending other users;
- Seeing "memories" of their friends and other users' profiles;
- Restriction of access to "memories" of users who are not in their friends list;
- Setting dark or light mode for the app;

Beer Diary provides all the functions only to authenticated users.

#### 3. Which technologies were used to develop this app?
  
  - Frontend: HTML5, CSS3 (+ Bootstrap), Javascript;
  - Backend: Django (Python);
  - Deployment: Heroku.

#### 4. What are all these files in this repository?
  
The organization of folders and files is the default organization provided by Django.

"Myapp" folder is the main folder of the app which provides main settings, main url routes and etc.

"Diary" folder is responsible for the main functions of the app, i.e. adding "memories", updating and changing "memories", so all the actions you can do with your beer diary "memories".

"Users" folder is responsible for user accounts, registering, logging in, adding friends, seeing users' profiles.

All the database models can be found in models.py files.

All the view functions (functions and Django classes which are the controllers of the app) can be found in views.py files.

Forms.py files contain forms classes for GET and POST forms.

Urls.py files contain routing settings.
