'''Write a function that takes a Python dictionary and writes it to a JSON file. The dictionary should contain the following keys: username (string), age (integer), and hobbies (list of strings). The file should be written in text mode with the filename "user_data.json".

Test your function with a dictionary containing sample data and ensure that the dictionary is properly serialized into the JSON file.'''


'''PSEUDOCODE
- IMPORT JSON
- CREATE A PYTHON DICTIONARY GLOBALLY.
- CREATE A JSON FILE GLOBALLY
- CREATE FUNCTION dict_conv
- FUNCTION TAKES PYTHON OBJ(DICT)
- USE OPEN FUNCTION TO WRITE TO JASON FILE
- USE JSON DUMP FUNCTION TO SERIALIZE DICT TO JSON FORMAT
- PRINT OUTPUT'''

import json
books = {
    "title": "Great Expectations",
    "author" : "Charles Dickens",
    "ISBN" : 82726
}

FILENAME = "file.json"
def dict_conv(obj):
    with open(FILENAME, 'w') as f:
     json.dump(obj, f)
     print(f'This is the serialised file output: {json.dumps(obj, indent=4)}')

dict_conv(books)
    
    