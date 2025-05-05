# Define a dictionary called `car` with some key-value pairs
car = {
    "make" : "ford",            # The car's make is 'ford'
    "model" : "modeo",          # The car's model is 'modeo'
    "year"  : 2006,             # The year of manufacture is 2006
    "owner" : {                 # Nested dictionary for the owner's details
        "name" : "andrew",          # Owner's name is 'andrew'
        "driver-number": 1123       # Driver number assigned is 1123
    }
}

# Print the value associated with the "year" key (2006)
print(car["year"])

# Access the nested dictionary under "owner", and then print the value for the key "name" ("andrew")
print(car["owner"]["name"])

# Use the .get() method to try to retrieve the value for the key "names" in the nested "owner" dictionary.
# Since "names" does not exist, .get() returns None.
# Then, type() checks the data type of the returned value, which is <class 'NoneType'>
print(type(car["owner"].get("names")))
