'''Exercise: Write and Read a Name from a File

Write a Python program that:

Asks the user to enter their name.
Saves the name to a file called name.txt.
Reads the name back from the file.
Prints a message like "Hello, <name>!"'''


'''PSEUDOCODE
1. USER INPUT - NAME
2. ASSIGN INPUT TO VAR FILENAME
2. CREATE A FILE USING WRITE
3. ASSIGN FILENAME VAR to name.txt
4. READ FROM FILE
5. DISPLAY CONTENT FROM FILE 
'''

name = input('please enter your name: ')

with open("name.txt", "w") as f:
     f.write(name)

with open("name.txt", "r") as f:
    output = f.read()
    print(output)



'''# Ask user for their name
name = input('Please enter your name: ')

# Save the name to a file
with open("name.txt", "w") as f:
    f.write(name)

# Read the name back from the file
with open("name.txt", "r") as f:
    output = f.read()

# Display a personalized message
print(f"Hello, {output}!")
'''
