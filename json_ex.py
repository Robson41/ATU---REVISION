# Import the JSON module, which allows us to work with JSON data.
import json

# Define the filename where the JSON dictionary will be saved.
FILENAME = "testdict.json"

# Create a sample dictionary with some data.
# This dictionary contains a name (string), age (integer), and grades (list of integers).
sample = dict(name='andrew', age=99, grades=[1, 34, 55])

# Function to write the dictionary object to a JSON file
def writeDict(obj):
    # Open the file in write mode ('wt' means text mode).
    # If the file does not exist, it will be created.
    with open(FILENAME, 'wt') as f:
        # Use json.dump() to convert the dictionary into a JSON string and write it to the file.
        # The `obj` is the dictionary to be saved in JSON format.
        json.dump(obj, f)

# Test the function by calling it with the 'sample' dictionary.
writeDict(sample)
