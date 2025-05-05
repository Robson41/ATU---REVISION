'''Create a dictionary called book that contains the following keys and values:
"title": "The Hobbit"
"author": "J.R.R. Tolkien"
"year": 1937
"genres": a list with the values "Fantasy", "Adventure"
Then, write Python code to:
Print the author's name.
Print the first genre in the list.
Print the type of the value stored in "genres".'''

book = {
"title": "The Hobbit",
"author": "J.R.R. Tolkien",
"year": 1937,
"genres" : { 
    "genre_1" : "Fantasy", 
    "genre_2" : "Adventure",
}
}

print(book["genres"]["genre_1"])
print(type(book["genres"]))
