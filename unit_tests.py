#!/usr/bin/python
# analyze gendered words


import os
#from wordlists.gender_words import MALE_WORDS, FEMALE_WORDS
from analyze.gender import gender_ratio
from analyze.gender import word_counter
from analyze.gender import both_genders
from analyze.gender import gender

sample_text = "she was lifting weights while he was sewing the clothes. his wife noticed that \
her husband was talking to his grandmother who was also the queen. she knew of a prince who \
was a priest "

text = sample_text

print word_counter(text)

clean_text = text
print gender(clean_text)

print both_genders(clean_text)

"""
Female gendered: 5
she, wife, her, grandmother, she
Male gendered: 6
he, his, husband, his, prince, priest
"""



if __name__ == '__main__':
	assert 1+1
	

