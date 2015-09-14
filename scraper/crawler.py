#!/usr/bin/python -tt
#crawls a project gutenberg and returns name of bookname and url

from bs4 import BeautifulSoup
import requests
import os

BASE_URL = "https://www.gutenberg.org/wiki/Science_Fiction_(Bookshelf)"
filename = "gutenberg_bookshelf.txt"

def bookshelf_html(BASE_URL):
    'requests html from gutenberg bookshelf page'

    r = requests.get(BASE_URL, verify = False)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    return soup

def write_file(soup):
    
    if os.path.isfile(filename):
        print "file exists"
    else:
        with open(filename, "w") as f:
                soup = str(make_soup(BASE_URL)) ###<---was it ok to convert it to a str?
                f.write(soup) 

def read_file(filename):
    
    with open(filename, "r") as f:
        #htm = json.load(f)
        html = f.read()
    
    return html

def extract_text_urls(filename):
    'extracts bookname and urls'
    
    html = read_file(filename)
    
    for a in html.findAll('a'):
        data = a['title'], a['href']
    print data
    
    ##this function is not working, i am getting AttributeError: 'str' object has no attribute 'findAll'

def extracts_book_info():
    ''
    pass
    
bookshelf_html(BASE_URL)
write_file(soup)
read_file(filename)
extract_text_urls(filename)

if __name__ == '__main__':
    assert 1+1