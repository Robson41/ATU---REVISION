'''Create a Python script that stores information about three countries in a dictionary.
Each country should have the following details stored as a nested dictionary:

Capital city
Population (in millions)
Currency


Use a for loop with .items() to iterate over each country and print:
The name of the country
Its capital
Its population
Its currency
(Use proper formatting for clarity.)'''

Country = {
    "Germany": {
    "Capital_City" : "Berlin",
    "Population" : 10000000,
    "Currency" : "euro"
    },

    "Japan" : {
    "Capital_City" :  "Tokyo",
    "Population" : 6000000,
    "Currency" : "yen",
    },

    "America" : {
     "Capital_City" : "Washington",
     "Population" : 7000000,
     "Currency" : "dollar"
    }
}

for key, value in Country.items():
    print(f'"This is the Country: {key}, and its attributes are the following: {value}')