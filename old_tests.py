#!/usr/bin/python
# analyze gendered words


import os
import unittest
from analyze.gender import gender_ratio
from analyze.gender import word_counter
from analyze.gender import both_genders
from analyze.gender import gender
from wrangle.read import remove_punc_html
from analyze.gender import gender_ratio
from scraper.gutenberg_engine import get_book_text

text = "<h1>She was lifting weights while he was sewing clothes. His wife noticed that \
her husband was talking to his grandmother's ghost who was also the princess! The priest was the prince. </h1>"

def test_removing_punctuation(text):
    return remove_punc_html(text)
    
def test_counting_words(text):
    text = test_removing_punctuation(text)
    word_dict = word_counter(text)
    return sum(word_dict.itervalues())

def test_printing_gender_dict(text):
    clean_text = remove_punc_html(text)
    return gender(clean_text)

def test_printing_both_genders_dict(clean_text):
    clean_text = remove_punc_html(text)
    return both_genders(clean_text)

def test_printing_gender_ratio(clean_text):
    clean_text = remove_punc_html(text)
    return gender_ratio(clean_text)

csvfile = "gutenbergscifi.csv"
def test_extracting_book_test(csvfile):
    text = get_book_text(csvfile)
    return text

###TESTS
print "TEST: Assert if punctuation and html are removed and if text is lower case"
print test_removing_punctuation(text)
assert "she was lifting weights while he was sewing clothes his wife noticed that her "
"husband was talking to his grandmothers ghost who was also the princess the priest was "
"the prince " == test_removing_punctuation(text)

print "TEST: Assert if all the words in the text are counted correctly"
print test_counting_words(text)
assert 31 == test_counting_words(text)
#self.assertEqual(test_counting_words(text),31")

print "TEST: If correct gendered words and count are printed"
print test_printing_gender_dict(text)
# assert "defaultdict(<type 'int'>, {u'his': 2, u'her': 1, u'wife': 1, u'grandmothers': 1, "
# "u'prince': 1, u'priest': 1, u'she': 1, u'princess': 1, u'husband': 1, u'he': 1})" == test_printing_gender_dict(text)

print "TEST: If gendered word counts are returned in a tuple (e.g., (M words, F words))"
print test_printing_both_genders_dict(text)
assert (6, 5) == test_printing_both_genders_dict(text)

print "TEST: If male to female ratio is printed correctly"
print test_printing_gender_ratio(text)
assert 1.2 == test_printing_gender_ratio(text)

print "TEST: If correct book number is returned for each book"
print test_extracting_book_test(csvfile)
# assert "0 29882 \
# 1 30177 \
# 2 41027 \
# 3 24091 \
# 4 29579 \
# 5 29353 \
# 6 42914 \
# 7 18846 \
# None" == test_extracting_book_test(csvfile)


class TestMethods(unittest.TestCase):

  def test_gender_dict(self):
      self.assertEqual(test_counting_words(text),31)

"""
Male gendered: 6
he, his, husband, his, priest, prince
Female gendered: 5
she, wife, her, grandmothers, princess

"""

if __name__ == '__main__':
	assert 1+1
	

