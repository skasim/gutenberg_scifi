#!/usr/bin/python -tt
# read a file and save it to memory

import os
from bs4 import BeautifulSoup
from string import punctuation
import string
import nltk
from nltk.corpus import stopwords


def read_file(filename):
    
    with open(filename, 'r+') as file_ref:
          
          text = file_ref.read()

    return text
    
def remove_punc_html(text):
   
    exclude = set(string.punctuation)
    text = BeautifulSoup(text, "html.parser").findAll(text = True)
    text = [word.lower() for word in text if word not in exclude]
    text = ' '.join(word for word in text if word not in stopwords.words('english'))
    #the above is removing stopwords, not sure if there is a more efficient way to write this out
    #is this correct: split() splits a string by the white space into an item in a list and x.join, joins an item into a string at x[or whatever else is there]
    #rewrite as class
    return text
    
    
    
if __name__ == '__main__':
    filename = os.path.expanduser("~/Desktop/scifi/data/frank_text.txt")
    read_file(filename)
    text = read_file(filename)
    print remove_punc_html(text)