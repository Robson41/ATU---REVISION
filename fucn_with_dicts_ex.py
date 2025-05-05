'''You are tasked with creating a program to manage a list of books in a library. Each book will have a title, author, and a list of genres. Your task is to implement the following functions:

readGenres(): This function should return an empty list, representing the genres of a book. This is a placeholder for now, but it can be expanded later to accept user input for genres.
addBook(): This function should take a list of books and:
Prompt the user to enter the book's title.
Prompt the user to enter the book's author.
Use the readGenres() function to get the genres (for now, this should return an empty list).
Add the book (represented as a dictionary with title, author, and genres) to the list of books.'''

books = [{}]

book = {
"title" : "kidnapped",
"author": "enid blython",

"genres" :{
    "genre_1" :  "fantasy",
    "genre_2" : "adventure"
}

}

def readGenres():
    return []

def adBook(books):
    title = input('Please enter the books title: ')
    author = input('Please enter the books author: ')


readGenres(book)
book = input('Please enter genre, title and author')



