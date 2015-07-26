#!/usr/bin/python -tt
# read a file and save it to memory

import os
from bs4 import BeautifulSoup
import string


def read_file(filename):
    
    with open(filename, 'r+') as file_ref:
          
          text = file_ref.read()

    return text
    
def remove_html(text):
    
    text =  ''.join(BeautifulSoup(text, "html.parser").findAll(text = True)) 
    return text
    
def remove_punc(text):

    pass
    
    
if __name__ == '__main__':
    filename = os.path.expanduser("~/Desktop/scifi/data/frank_text.txt")
    read_file(filename)
    text = read_file(filename)
    print remove_html(text)