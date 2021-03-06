#!/usr/bin/python -tt
# execute code

import os
import json

from scraper.crawler import extract_text_urls
from scraper.crawler import open_csv
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from wrangle.read import remove_punc_html
from analyze.gender import gender_ratio
from engine.engine_json import load_or_create_json
from engine.engine_json import write_json
from engine.engine_json import read_write_json_object

def main():
    filename = "gutenbergscifi.csv"
    json_filename = "gendered_words.json"
    
    if os.path.isfile(filename):
        print "file exists"
        
    else:
        write_csv = extract_text_urls(filename)
        print "file created"

    book_list = open_csv(filename)
    
    print book_list
    
    for i, value in enumerate(book_list):
        #print i, value
        
        a = int(book_list[i][2]) # a = book number
        print i, a
        author = book_list[i][0]
        title = book_list[i][1]
        try:
            text = strip_headers(load_etext(a)).strip()
        except ValueError:
            pass
        #print text  
        
        clean_text = remove_punc_html(text)
        ratio = gender_ratio(clean_text)
        
        print author, title, ratio
        uber_key = author
        sub_key = title
        sub_value = ratio
        uber_value = {author: {title:ratio}}

        json_source = read_write_json_object(json_filename="gendered_words.json", uber_key=uber_key, uber_value=uber_value, sub_key=sub_key, sub_value=sub_value, READ=False, WRITE=True)
        


if __name__ == '__main__':


    assert 1+1


    main()