'''Write a Python script that:

Takes a filename as a command-line argument.
Attempts to open and read the file.
If the filename is not provided, catch the IndexError and print a helpful message.
If the file does not exist, catch the FileNotFoundError and print an appropriate error message.
If successful, print the contents of the file.'''

'''PSEUDOCODE
- Import sys module
- Assign the argument to filename
- Add a try to begin validation of file interaction
- Use read to open file
- Use IndexError validation to check if any argument has been entered
- Also use Filenotfound validation to check if file exists
- Only if successfull, print contents of file


import sys

try:

    filename = sys.argv[1]
    print(f'{filename}')

    with open(filename, 'r') as f:  
        f.read()

except IndexError:
    print("No File has been read in from command line")'''

import sys

print("sys.argv:", sys.argv)  # Print sys.argv to debug

try:
    filename = sys.argv[1]
    print(f'{filename}')

    with open(filename, 'r') as f:  
        f.read()

except IndexError:
    print("No File has been read in from command line")

except FileNotFoundError:
    print(f"File {filename} not found")







