#!/usr/bin/python -tt
# read a file and save it to memory

import os
from bs4 import BeautifulSoup
from string import punctuation
import string
import nltk
from nltk.corpus import stopwords


def read_file(filename):
    "reads file and returns the text"
    
    with open(filename, 'r+') as file_ref:
          
          text = file_ref.read()

    return text
    
def remove_punc_html(text):
    "removes punctuation and letters in lower case and returns clean text"
   
    exclude = set(string.punctuation)
    text = BeautifulSoup(text, "html.parser").findAll(text = True)
    
    text = [letter.lower() for word in text for letter in word if letter not in exclude]
    text = ''.join(word for word in text)
    #text = [word.lower() for word in text if word not in exclude]
    #text = ' '.join(word for word in text if word not in stopwords.words('english'))
    #rewrite as class
    return text
    
    
    
if __name__ == '__main__':
    filename = os.path.expanduser("~/Desktop/scifi/data/frank_text.txt")
    read_file(filename)
    text = read_file(filename)
    print remove_punc_html(text)