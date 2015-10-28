#!/usr/bin/python -tt
#crawls a project gutenberg and returns name of bookname and url

from bs4 import BeautifulSoup
import requests
import os
import csv

BASE_URL = "https://www.gutenberg.org/wiki/Science_Fiction_(Bookshelf)"
filename = "gutenberg_bookshelf.txt"
csvfile = "gutenbergscifi.csv"


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

def write_csv(data):
    
    with open("gutenbergscifi.csv", "a") as f:
        author, title, url = data
        row = author + ";" + title + ";" + url + "\n"
        f.write(row) 

    
def extract_text_urls(html):
    'extracts bookname and urls'
    
    soup = make_soup(BASE_URL)
    author = "none, none"
    #soup = read_write_file(filename) #<---why doesn't this work
    
    #for li in soup.findAll('li'):#, class_= "extiw"):
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
                    data = author, title, url.replace("//www.gutenberg.org/ebooks/","")
                    print data###<----why does this only print out 1 line
                    try:
                        write_csv(data)
                    except UnicodeEncodeError:
                        pass
                except KeyError:
                    pass
            except TypeError:
                pass


def open_csv(csvfile):
    'opens and reads csv file and returns a list'
     
    with open(csvfile,"rU") as f:
        text = csv.reader(f, delimiter =";")
        book_list = list(text)
    
    return book_list
    
        


if __name__ == '__main__':
    assert 1+1
    
    
"""
Note on the Project Gutenberg HTML page:

DON'T USE THIS PAGE FOR SCRAPING.
Seriously. You'll only get your IP blocked.
Download http://www.gutenberg.org/feeds/catalog.rdf.bz2 instead,
which contains *all* Project Gutenberg metadata in one RDF/XML file.
"""