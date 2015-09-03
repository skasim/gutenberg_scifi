#!/usr/bin/python
# analyze gendered words

from __future__ import division
import os
from wordlists.gender_words import MALE_WORDS, FEMALE_WORDS
from collections import defaultdict



def word_counter(text): #opens the file and reads file. 
    """ 
    input: cleaned text file


    output: dictionary or 
    """


    word_dict = {}
    
    words = text.split() #splits the text into separate words
    
    for word in words:
        
        if word not in word_dict: # --> Think about collections - counter on this
            word_dict[word] = 1
        else:
            word_dict[word] = word_dict[word] + 1    
    
    # for key in sorted(word_dict, key = word_dict.get, reverse = False):
    #         print "%s: %s" % (key, word_dict[key]) #if i return this, it only prints one line
            
    return word_dict


def gender(clean_text):
    
    gender_words_set = MALE_WORDS.union(FEMALE_WORDS)
    gender_dict = defaultdict(int)
    words = clean_text.split()
    
    for word in words:
        if word in gender_words_set:
            gender_dict[word] += 1
            
    return gender_dict
    
     

def both_genders(clean_text):

    male_dict = defaultdict(int)
    female_dict = defaultdict(int)
    words = clean_text.split()
	
    for word in words:
        if word in MALE_WORDS:
            male_dict[word] += 1
        elif word in FEMALE_WORDS:
            female_dict[word] += 1
            
    male_sum = sum(male_dict.values())
    female_sum = sum(female_dict.values())
    
    return male_sum, female_sum #did you want it to be more like ((male sum: X), (female sum:Y)). i am not sure i know how to do that

def gender_ratio(clean_text):
    
    gender_sums = both_genders(clean_text)
    male_sum, female_sum = gender_sums
    gender_ratio = round(male_sum/female_sum,2)
    
    return gender_ratio

if __name__ == '__main__':
	print MALE_WORDS, FEMALE_WORDS