import json

# Define the file name to store the dictionary
FILENAME = "testdict.json"

def readDict():
    # This will throw an error if the file does not exist or cannot be opened
    # In the future, we can handle this case and return an empty dictionary or a default value
    with open(FILENAME) as f:
        # Load and return the content of the JSON file as a Python dictionary
        return json.load(f)

# Test the function
somedict = readDict()
# Print the dictionary loaded from the JSON file
print(somedict)
