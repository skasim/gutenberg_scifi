#!/usr/bin/python -tt
#crawls project gutenberg catalog and gets text


from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from scraper.cralwer import get_book_text

def get_book_text(csvfile):
    'gets text for book using project gutenberg catalog'
    book_list = open_csv(csvfile)
    
    for i in range(len(book_list)):
    
        a = int(book_list[i][2]) # a = book number
        print a
        text = strip_headers(load_etext(a)).strip()
        
        return(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'

"""
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

text = strip_headers(load_etext(22538)).strip()
print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'

from gutenberg.query import get_etexts
from gutenberg.query import get_metadata
"""

if __name__ == '__main__':
    assert 1 + 1
