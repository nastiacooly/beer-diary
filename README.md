# Beer Diary
## A web-app to keep memories of all the beers you ever tasted and share it with friends!

#### Go to <URL> to try Beer Diary yourself!
#### Video Demo:  <URL HERE>

  
#### What is it?
  
Beer Diary is my final project for CS50: Introduction to Computer Science course.

Beer Diary is a web-application created with help of Django framework (used Python, Javascript, HTML5, CSS3).

Developed in 2021 by Anastasia Maryina (@nastiacooly).

#### What can it do?
  
Beer Diary provides the following experience for users:
  
- users can register their accounts, log in with their account to the app;
- users can add "memories" of beer to their Beer Diary;

"Memories" are like beer reviews where user can write his/hers impressions from a beer.
Memory consists of a beer name, beer image, beer type (for example, stout or lager), beer rating (from 1 to 5 stars) and additional optional comments.

- users can update and delete their "memories";
- users can see all their "memories" in a list for easy access;
- users can search their "memories" by a beer name;
- users can filter their "memories" by different characteristics such as beer type, filtered or unfiltered beer, light or dark beer and beer rating;
- users can see their favourite "memories" (i.e., all the beers with 5-star rating);
- users can search other users and add friends;
- users can see their profiles with account info, statistics (number of "memories" and etc.) and friends;
- users can accept, reject and cancel friend requests and unfriend other users;
- users can see "memories" of their friends and friends' profiles;
- users can set dark or light mode for the app.

#### Which technologies were used to develop this app? And how does it work?
  
Well, as I mentioned, Beer Diary was developed with help of Django Framework.

So, the most of the code is written in Python.

Templates for pages of the app were made with HTML5, CSS3 and also Python.

Interactive elements and switching of dark/light mode was developed with Javascript.

#### What are all these files in this repository?
  
The organization of folders and files is the default organization provided by Django.

"Myapp" folder is the main folder of the app which provides main settings, main url routes and etc.

"Diary" folder is responsible for the main functions of the app, i.e. adding "memories", updating and changing "memories", so all the actions you can make with your beer diary "memories".

"Users" folder is responsible for user accounts, registering, logging in, adding friends, seeing users' profiles.

All the database models can be found in models.py files.

All the view functions (functions and Django classes which are the controllers of the app) can be found in views.py files.

Forms.py files contain forms classes for GET and POST forms.

Urls.py files contain routing settings.
