'''Write a Python program that:
Asks the user for the name of a text file.
Attempts to open the file in read mode.
If the file exists, it prints the contents to the screen.
If the file doesn’t exist, it shows an error message (use try/except).
Bonus: After printing the content, also print the number of lines in the file.'''

try:
    with open("test.txt","r")as f:
            data = f.read()

            print(data)
except FileNotFoundError:
     print("file does not exist")
    
    
    