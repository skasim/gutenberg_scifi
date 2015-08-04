#!/usr/bin/python -tt
# open a file from project Gutenberg and save it to a variable

import os
import requests


def open_file(files): #downloads the book from Project Guttenburg and writes to a file


    url, text_name = files


    text_name = 'data/' + text_name

    if os.path.isfile(text_name):
        #print "%s file already here" % text_name # ->> NJD

        pass
        
    else:
        # print url, text_name
        text_file = requests.get(url, verify = False)
        text_file = text_file.content
        file_ref = open(text_name,"w+")
        file_ref.write(text_file)
        # print '%s file downloaded' % text_name # ->> NJD
    
    return text_name     

def open_several_files(files):
    
    for afile in files:
        open_file(afile) #is open_file a python term for opening a file?

    return [text_name for url, text_name in files]
    
    

if __name__ == '__main__':
	files = [['https://www.gutenberg.org/files/84/84-h/84-h.htm', 'frank_text.txt'],
        ['https://www.gutenberg.org/cache/epub/42/pg42.html', 'dr_JEKYLL.txt']
        ]
	assert open_several_files(files) == ['frank_text.txt', 'dr_JEKYLL.txt']