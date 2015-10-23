## Scifi Project

Analyze scifi books on Project Gutenberg


## Goals

Collect, wrangle, analyze and present insights on a web app from freely available works of 
science fiction on Project Gutenberg.


## To Set Up

- pip install requirements into a virtualenv called scifi
- pip install gutenberg


## To Run

Run in terminal by **admin_gender.py**

## To Do

1.  Check to see if csv  file exists already. if yes, skip to step 4. if no, go to step 2 and 3 [done].
2.  Go to Project Gutenberg scifi bookshelf [done].
3.  Scrape form the bookshelf the names, title, and urls of all scifi books and add them to a csv file [done].
4.  Access and read the csv file [done].
5.  For reach url in the file access the book text using the gutenberg module [done].
6.  Read each text and identify the male-female gendered words ratio [done].
7.  Add the {author:{title, ratio} to json data source[done].
8.  Test code with larger data set.
9.  Build a web app with Flask.
10.  Create unit tests.
11.  Add more gendered words to gender_words.py.
