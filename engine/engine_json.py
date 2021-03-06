#!/usr/bin/python -tt
# phase one - data store for dict-like objects with read and write
# phase two - data store object


import json
#print json.__file__
#/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/__init__.pyc
import os
import collections

#json_filename = "gendered_words.json"


#### Create JSON Engine

def write_json(json_filename, gender_dict):
    "writes json object"
    with open (json_filename, "w") as json_filename:
        data = json.dump(gender_dict, json_filename)
        
    return "written to file"
    
def load_json(json_filename):
    "loads json object"
    with open (json_filename, "r") as json_file:
        data = json.load(json_file)
        print 'opened!'
    
    return data
    
def create_json(json_filename):
    "creates json file"
    
    with open (json_filename, "w") as json_file:
        print "creating file"
        data = {}
        
        return data

def load_or_create_json(json_filename):
    "Checks to see if json object exists and then loads it, else creates json and loads it"

    if os.path.isfile(json_filename):
        data = load_json(json_filename)
        
    else:
        data = create_json(json_filename)

    return data # returns a python dict


#### Read / Write of keys into json object
"""
   Checks if json datastore is created, if not creates it
   Checks for for key in datastore, if yes updates key-values, otherwise adds new key-value
"""

def read_write_json_object(json_filename=None, uber_key=None, uber_value=None, sub_value=None, sub_key=None, READ=False, WRITE=False):

    data = load_or_create_json(json_filename)
    
    if WRITE:
        if data.get(uber_key):
            print "%s key already present" % uber_key
            if uber_value in data.values():
                print "%s  value already present" % uber_value
            else:
                #data[uber_key].append(uber_value)
                data[uber_key][sub_key] = [sub_value]
                print "new value added to existing key"
                write_json(json_filename, data)
        else:
            data.update({uber_key: uber_value})
            print "key added"
            write_json(json_filename, data)
    elif READ:
        return data.get(uber_key, None)
    else:
        print "pick read or write"
        raise Exception("fix me")   



if __name__ == '__main__':
    assert 1+1