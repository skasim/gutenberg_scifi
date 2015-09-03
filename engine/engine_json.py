#!/usr/bin/python -tt
# phase one - data store for dict-like objects with read and write
# phase two - data store object


#python module called json (to import) import json.loads

import json
#print json.__file__
#/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/__init__.pyc
import os

json_dict = {
    "id": 1,
    "name": "A green door",
    "price": 12.50,
    "tags": ["home", "green"]
}
filename = "test.json"

#### Create JSON Engine

def create_json(filename):
    'creates json file'
    if os.path.isfile(filename):
        print "file exists"
        pass
    else:
        with open (filename, "w") as f:
            print "creating file"
            pass
            
def write_json(filename, json_dict):
    "writes json object"
    with open (filename, "w") as filename:
        data = json.dump(json_dict, filename)
        
    return "written to file"
    
    
        #with open("firstlevel_urls.txt", 'w+') as f:
        #data = json.dump(url_list, f)  

def load_json(filename):
    "loads json object"
    with open (filename, "r") as json_file:
        data = json.load(json_file)
        print 'opened!'
    
    return data


def load_or_create_json():
    ' Checks to see if json object exists and then loads it, else creates json and loads it '
    #to check if something exists use os
    pass


#### Read / Write of keys into json object


def read_json(key):
    '''
    checks loaded json object for key

    if key exists, returns values into python readable format

    else returns, None / False

    '''
    
#     if key in filename:
#         print key
#         
#     else:
#         print "False"
#     
    data = load_json(filename)
    
    
    if key in data:
        print key, data[key]
    
    else: 
        return None
    


def write_dict_json(json_dict):
    'writes python dictionaries (key-value) into json object'
    
    data = load_json(filename)
    json_dict[new_k] = [new_v]
    #print data
    print json_dict

##### Data Store (json) engine

def json_read_engine(python_dict):
    """
    Checks if json datastore is created, if not creates it

    Checks for key in datastore and returns value, else returns none

    """

def json_write_engine(python_dict):
    """
    Checks if json datastore is created, if not creates it

    Checks for for key in datastore, if yes updates key-values, otherwise adds new key-value

    """



create_json(filename)
write_json(filename, json_dict)
load_json(filename)
key = "name"
read_json(key)
new_k ="color"
new_v = "blue"
write_dict_json(json_dict)

if __name__ == '__main__':
    assert 1+1