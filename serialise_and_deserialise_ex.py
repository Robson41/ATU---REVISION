'''Question:
Write a Python program that does the following:

Creates a Python dictionary with at least three key-value pairs.
Serializes the dictionary and writes it to a JSON file using json.dump().
Opens the file, reads its content as a string, and then deserializes the JSON string back into a Python dictionary using json.loads().
Prints the final Python dictionary to the console.'''

'''PSEUDOCODE

- import json
- Create py_dict
- Create ser_deser func
- Create json file
- Use open func and write mode
- Serialise to json using dump
- use Open file and read mode
- Deserialise back to python_dict
- Validation to ensure it was serialised
- return value
- call func
- assign to var
- print var'''

import json 
books = {
    "title" : "Great Expectations",
    "author" : "Charles Dickens",
    "ISBN" : 98273
}

filename = 'txt.json'

def ser_deser(obj):
    with open(filename, 'w')as f:
       json.dump(obj, f)

    with open(filename, 'r') as fd:
      pyt_dict = json.load(fd)
      if pyt_dict == books:
         print(f'The {obj} dictionary was successfully serialised and deserialised')
    return obj


output = ser_deser(books)

print(f'The final output is {output}')

    


