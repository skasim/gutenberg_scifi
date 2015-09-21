#!/usr/bin/python -tt
#crawls a project gutenberg and returns name of bookname and url

from bs4 import BeautifulSoup
import requests
import os

BASE_URL = "https://www.gutenberg.org/wiki/Science_Fiction_(Bookshelf)"
filename = "gutenberg_bookshelf.txt"


def make_soup(BASE_URL):
    'requests html from gutenberg bookshelf page'
    
    r = requests.get(BASE_URL, verify = False)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    return soup

def write_file(soup):
    'writes gutenberg bookshelf page html to a file'
    
    soup = make_soup(BASE_URL)
    
    if os.path.isfile(filename):
        print "file exists"
    else:
        with open(filename, "w") as f:
                soup = str(make_soup(BASE_URL)) ###<---ok to convert to a string?
                f.write(soup) 

def read_file(filename):
    'reads gutenberg bookshelf page html'
    
    with open(filename, "r") as f:
        #html = json.load(f)
        html = f.read()
    
    return html

def read_write_file(filename):
    'checks to see if file exists. if yes, reads it to data, if no, writes it to data'

    if os.path.isfile(filename):
        data = read_file(filename)
        
        return data
    else:
        soup = make_soup(BASE_URL)
        data = write_file(soup)
        
        return data


def extract_text_urls(html):
    'extracts bookname, urls, and author'
    
    soup = make_soup(BASE_URL)
    author = "n/a"
    #soup = read_write_file(filename) #<---why doesn't this work
    
    for h3 in soup.findAll('h3'):
        try:
            h3.a['title']
            author = h3.a.contents[0]
        except TypeError:
            pass
        for li in soup.findAll('li'):
            try:
                try:
                    url = li.a['href']
                    title = li.a.contents[0]
                    print url, title, author #if i use return it only returns 1 line
                except KeyError:
                    pass
            except TypeError:
                pass


if __name__ == '__main__':
    assert 1+1
    
    
"""
Note on the Project Gutenberg HTML page
DON'T USE THIS PAGE FOR SCRAPING.

Seriously. You'll only get your IP blocked.

Download http://www.gutenberg.org/feeds/catalog.rdf.bz2 instead,
which contains *all* Project Gutenberg metadata in one RDF/XML file.
"""