# #!/usr/bin/python -tt
# phase one - data store for dict-like objects with read and write
# phase two - data store object



#### Create JSON Engine

def load_json():
    "loads json object"


def create_json():
    'creates json file'
    pass


def load_or_create_json():
    ' Checks to see if json object exists and then loads it, else creates json and loads it '

    pass


#### Read / Write of keys into json object


def read_json(key):
    '''
    checks loaded json object for key

    if key exists, returns values into python readable format

    else returns, None / False

    '''
    pass


def write_json(python_dict):
    'writes python dictionaries (key-value) into json object'
    pass


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


