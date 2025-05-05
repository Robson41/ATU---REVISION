'''Write a function that reads a JSON file and returns its contents as a Python dictionary using json.load(). The function should not handle errors, but if the file is empty or does not exist, an error will occur.

'''

'''PSEUDOCODE
- Import Json
- Create json dictionary
- Create json file
- Create de_serialise function that accepts a json object
- Use open function with read mode to read json file
- Use json load to deserialise
- Ensure Output is displayed
- Call function'''

import json

# Step 1: Create the data.json file with JSON data (serialize)
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

FILENAME = "data.json"

# Writing the dictionary to the JSON file
with open(FILENAME, 'w') as f:
    json.dump(data, f, indent=4)

print(f"The data has been written to {FILENAME}")

# Step 2: Read the content of the file and deserialize it using json.loads()
with open(FILENAME, 'r') as f:
    file_content = f.read()  # Read the file content as a string
    python_dict = json.loads(file_content)  # Deserialize the string into a Python dictionary

print("Deserialized Python Dictionary:")
print(python_dict)
