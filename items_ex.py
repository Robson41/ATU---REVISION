# Define a dictionary named 'car' with details about a car
car = {
    "make": "Fiat",                         # 'make' is a key with the value "Fiat"
    "model": "Punto",                      # 'model' is a key with the value "Punto"
    "price": 10000,                        # 'price' is a key with the numeric value 10000
    "tags": ["pre-owned", "Best Buy", "Dealer"]  # 'tags' is a key with a list of strings as its value
}

# Loop through each key-value pair in the dictionary using .items()
# .items() returns a view object that contains a list of dictionary's key-value tuple pairs
for key, value in car.items():
    # In each loop, 'key' will be the dictionary key (like "make", "model", etc.)
    # and 'value' will be the value associated with that key (like "Fiat", "Punto", etc.)
    print(key + ' has a value', value)
