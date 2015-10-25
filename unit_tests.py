#!/usr/bin/python
# analyze gendered words


import os
from analyze.gender import gender_ratio
from analyze.gender import word_counter
from analyze.gender import both_genders
from analyze.gender import gender
from wrangle.read import remove_punc_html
from analyze.gender import gender_ratio

text = "<h1>She was lifting weights while he was sewing clothes. His wife noticed that \
her husband was talking to his grandmother who was also the princess. The priest was the prince. </h1>"

def test_removing_punctuation(text):
    return remove_punc_html(text)
    
def test_counting_words(text):
    text = test_removing_punctuation(text)
    return word_counter(text)

def test_printing_gender_dict(text):
    clean_text = remove_punc_html(text)
    return gender(clean_text)

def test_printing_both_genders_dict(clean_text):
    clean_text = remove_punc_html(text)
    return both_genders(clean_text)

def test_printing_gender_ratio(clean_text):
    clean_text = remove_punc_html(text)
    return gender_ratio(clean_text)


###TESTS
print "TEST: Assert if punctuation and html are removed and if text is lower case"
print test_removing_punctuation(text)
#assert "she was lifting weights while he was sewing clothes. his wife noticed that \
#her husband was talking to his grandmother who was also the princess. the priest was a prince." == test_removing_punctuation(text)

print "TEST: If all the words in the text are counted"
print test_counting_words(text)


print "TEST: If correct gendered words and count are printed"
print test_printing_gender_dict(text)

print "TEST: If gendered word counts are returned in a tuple (e.g., (M words, F words)"
print test_printing_both_genders_dict(text)

print "TEST: If male to female ratio is printed correctly"
print test_printing_gender_ratio(text)

"""
Male gendered: 6
he, his, husband, his, priest, prince
Female gendered: 5
she, wife, her, grandmother, princess

"""



if __name__ == '__main__':
	assert 1+1
	

