'''Write a program that:

Prompts the user to enter text to save in a file.
If the file exists, append the new content to it.
If the file doesn't exist, create it and write the user input to the file.
The program should:

Display how many characters were written in each case.
Handle file operations in both write and append modes.
Hints:
Use "w" mode to create or overwrite a file.
Use "a" mode to append to an existing file.'''

usertext = input('Please enter text: ')

try:
    with open('new_file_text.txt', 'w') as f:
        data = f.write(usertext)
        print(data)
except FileNotFoundError:
    print('File does not exist')

'''try:
    with open('new_file_text.txt', 'r') as f:
        data = f.read(5)
        print(data)
except FileNotFoundError:
    print('File does not exist')'''

