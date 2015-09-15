#!/usr/bin/python -tt
# phase one - data store for dict-like objects with read and write
# phase two - data store object


#python module called json (to import) import json.loads

import json
#print json.__file__
#/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/json/__init__.pyc
import os

#### Create JSON Engine

def load_json(filename):
    "loads json object"
    with open (filename, "r") as json_file:
        data = json.load(json_file)
        print 'opened!'
    
    return data

def create_json(filename):
    'creates json file'
    with open (filename, "w") as json_file:
        print "creating file"
        data = json.load(json_file)
        return data
            
def write_json(filename, python_dict):
    "writes json object"
    with open (filename, "w") as filename:
        data = json.dump(python_dict, filename)
        
    return "written to file"
     




def load_or_create_json(filename):
    ' Checks to see if json object exists and then loads it, else creates json and loads it '
    #to check if something exists use os

    if os.path.isfile(filename):
        data = load_json(filename)
        
    else:
        data = create_json(filename)

    return data # returns a python dict




#### Read / Write of keys into json object


def read_json(key, filename=None): # Added key value argument for file
    '''
    checks loaded json object for key

    if key exists, returns values into python readable format

    else returns, None / False

    '''
       
    data = load_or_create_json(filename)
    
    # dictionaries have a get method... try it... what does it do?

    if key in data:
        return {key: data[key]} # returns it as a dictionary
    else: 
        
        return None
    


def write_dict_json(python_dict):
    'writes python dictionaries (key-value) into json object'
    
    data = load_json(filename)
    python_dict[new_k] = [new_v]
    
    # What about the write_json function to dump the python dict to a file? 

    print python_dict # print is for human, return is for computers (and humans on computers!!!)



##### Data Store (json) engine

def json_read_engine(filename=None, key=None):
    """
    Checks if json datastore is created, if not creates it

    Checks for key in datastore and returns value, else returns none

    """
    create_json(filename) # load_or_create? 
    
    # read_json? Or a custom function? Maybe the dictionary.get method?



def json_write_engine(python_dict):
    """
    Checks if json datastore is created, if not creates it

    Checks for for key in datastore, if yes updates key-values, otherwise adds new key-value

    """
    # This is a good attempt, it's evident that you're building a great understanding of functions and variables
    # I recommend you practice passing in variables into the function example: function(var1, var2, var3=None)
    # This will make your code much easier to read and recycle later on for other projects. 
    # You won't need to worry about global variables such as new_k or new_v not being there and breaking things.

    # For both the read and write methods of the json_engine, I recommend that you think about your helper functions and
    # designing them to reduce your workload (and amount of code to write). We can review this. =)
    

    create_json(filename)
    datastore = read_json(key)
    
    if datastore == None:
        write_dict_json(python_dict)
    else:
        python_dict[key] = [new_v]



python_dict = {
    "id": 1,
    "name": "A green door",
    "price": 12.50,
    "tags": ["home", "green"]
}
filename = "test.json"

create_json(filename)
write_json(filename, python_dict)
load_json(filename)
key = "name"
read_json(key)
new_k ="color"
new_v = "blue"
write_dict_json(python_dict)

if __name__ == '__main__':
    assert 1+1