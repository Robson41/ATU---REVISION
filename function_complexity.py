'''Certainly! Here's a similar exercise that involves interacting with the user to collect and store information. This time, we’ll ask the user to enter books for a reading list, including the book title, author, and year of publication. The challenge is to validate the inputs and handle edge cases like empty inputs or incorrect data formats.

Exercise: Managing a Reading List
Write a Python program that allows a user to create a reading list. The program should allow the user to enter the title, author, and year of publication for each book. The program should ensure that the user enters at least one book and that the year is a valid number. The program should allow the user to continue entering books until they choose to finish by leaving the title input blank.

Expected Functionality:
The user should be prompted to enter the title of the book.
If the user leaves the title blank, the program should stop and print the final reading list.
For each book entered, the program should ask for:
The book title (string).
The author (string).
The year of publication (integer).
If the user enters a non-integer value for the year, it should prompt them again until a valid integer is entered.
If the user tries to enter no books (i.e., they leave the title blank from the start), the program should print a message asking for at least one book to be entered.
After the user has finished entering books, the program should display a list of all entered books.
Example Interaction:
Enter book title (leave blank to finish): The Catcher in the Rye
Enter author: J.D. Salinger
Enter year of publication: 1951
Enter book title (leave blank to finish): To Kill a Mockingbird
Enter author: Harper Lee
Enter year of publication: 1960
Enter book title (leave blank to finish): 
Reading List:
1. "The Catcher in the Rye" by J.D. Salinger (1951)
2. "To Kill a Mockingbird" by Harper Lee (1960)
Hints:
You can use a while loop to repeatedly ask for book details.
Use try/except to handle the case when the user enters a non-integer value for the publication year.
You might want to store each book as a dictionary with title, author, and year as keys, and append each book to a list.'''

'''PSEUDOCODE

1. CREATE EMPTY READING LIST
2. CREATE BOOKS DICTIONARY
3. ASK USER TO KEY VALUE PAIRS IN DICTIONARY
4. USE IF AND LEN TO CHECK FOR EMPTY INPUTS
5. USE TRY EXCEPT VALUE ERROR TO HANDLE VALIDATION
6. ALLOW USER TO CONTINUE TO ENTER BOOK ENTRIES UNTIL CHOOSING TO FINISH BY LEAVING BLANK
7. PROGRAM SHOULD THEN PRINT THE READING LIST'''
def addbooks():
    reading_list = []

    while True:
        title = input("Please enter at least one title (leave blank to finish): ")
        if title == "":
            if len(reading_list) == 0:
                print("At least one title must be entered.")
                continue
            else:
                break

        author = input("Please enter an author: ")
        if author.strip() == "":
            print("Author cannot be empty.")
            continue

        while True:
            try:
                year = int(input("Please enter the year of publication: "))
                break  # Exit the year input loop only on valid entry
            except ValueError:
                print("Invalid year. Please enter a valid number.")

        # Build the book dictionary and add to the reading list
        book = {
            "title": title,
            "author": author,
            "publication year": year
        }
        reading_list.append(book)

    return reading_list

# Run it
reading_list = addbooks()

# Output nicely
print("\n📚 Your Reading List:")
for i, book in enumerate(reading_list, start=1):
    print(f"{i}. \"{book['title']}\" by {book['author']} ({book['publication year']})")

def addbooks():
    reading_list = []

    while True:
        title = input("Please enter at least one title (leave blank to finish): ")
        if title == "":
            if len(reading_list) == 0:
                print("At least one title must be entered.")
                continue
            else:
                break

        author = input("Please enter an author: ")
        if author.strip() == "":
            print("Author cannot be empty.")
            continue

        while True:
            try:
                year = int(input("Please enter the year of publication: "))
                break  # Exit the year input loop only on valid entry
            except ValueError:
                print("Invalid year. Please enter a valid number.")

        # Build the book dictionary and add to the reading list
        book = {
            "title": title,
            "author": author,
            "publication year": year
        }
        reading_list.append(book)

    return reading_list

# Run it
reading_list = addbooks()

# Output nicely
print("\n📚 Your Reading List:")
for i, book in enumerate(reading_list, start=1):
    print(f"{i}. \"{book['title']}\" by {book['author']} ({book['publication year']})")

def addbooks():
    reading_list = []

    while True:
        title = input("Please enter at least one title (leave blank to finish): ")
        if title == "":
            if len(reading_list) == 0:
                print("At least one title must be entered.")
                continue
            else:
                break

        author = input("Please enter an author: ")
        if author.strip() == "":
            print("Author cannot be empty.")
            continue

        while True:
            try:
                year = int(input("Please enter the year of publication: "))
                break  # Exit the year input loop only on valid entry
            except ValueError:
                print("Invalid year. Please enter a valid number.")

        # Build the book dictionary and add to the reading list
        book = {
            "title": title,
            "author": author,
            "publication year": year
        }
        reading_list.append(book)

    return reading_list

# Run it
reading_list = addbooks()

# Output nicely
print("\n📚 Your Reading List:")
for i, book in enumerate(reading_list, start=1):
    print(f"{i}. \"{book['title']}\" by {book['author']} ({book['publication year']})")

def addbooks():
    reading_list = []

    while True:
        title = input("Please enter at least one title (leave blank to finish): ")
        if title == "":
            if len(reading_list) == 0:
                print("At least one title must be entered.")
                continue
            else:
                break

        author = input("Please enter an author: ")
        if author.strip() == "":
            print("Author cannot be empty.")
            continue

        while True:
            try:
                year = int(input("Please enter the year of publication: "))
                break  # Exit the year input loop only on valid entry
            except ValueError:
                print("Invalid year. Please enter a valid number.")

        # Build the book dictionary and add to the reading list
        book = {
            "title": title,
            "author": author,
            "publication year": year
        }
        reading_list.append(book)

    return reading_list

# Run it
reading_list = addbooks()

# Output nicely
print("\n📚 Your Reading List:")
for i, book in enumerate(reading_list, start=1):
    print(f"{i}. \"{book['title']}\" by {book['author']} ({book['publication year']})")


