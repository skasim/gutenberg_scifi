#!/usr/bin/python -tt
# execute code

from scraper.ingest import open_several_files
from wrangle.read import read_file
from wrangle.read import remove_punc_html
from analyze.gender import word_counter
from analyze.gender import gender
from analyze.wordlists.gender_words import MALE_WORDS, FEMALE_WORDS
from analyze.gender import both_genders
from collections import defaultdict

def main():
    
    #filenames = open_several_files(files)
    
    #text = read_file(file)
    
    #clean_text = remove_punc_html(text)
    
    #word_counter(text)
    pass
     
    

if __name__ == '__main__':
	

	files = [['https://www.gutenberg.org/files/84/84-h/84-h.htm', 'frank_text.txt'],
        ['https://www.gutenberg.org/cache/epub/42/pg42.html', 'dr_JEKYLL.txt']
        ]

	assert open_several_files(files) == ['frank_text.txt', 'dr_JEKYLL.txt']
	
	text = read_file('data/frank_text.txt')
	
	clean_text = remove_punc_html(text)
	
	count_words = word_counter(clean_text)
	
	#gender_words_set = MALE_WORDS.union(FEMALE_WORDS)
	
	#print gender(clean_text, gender_words_set)
	
	#print both_genders(clean_text)
		
	#print count_words
	
	
	