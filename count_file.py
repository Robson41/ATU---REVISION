# Define the filename where the count is stored
FILENAME = "count.txt"

# Function to read the current count (number) from the file
def readNumber():
    # Open the file in read mode (default 'r') to read its contents
    with open(FILENAME) as f:
        # Read the content of the file, convert it to an integer, and return it
        number = int(f.read())  # Convert the string content of the file to an integer
        return number  # Return the number read from the file

# Function to write a number (updated count) to the file
def writeNumber(number):
    # Open the file in write mode ('wt') to overwrite the content of the file
    with open(FILENAME, "wt") as f:
        # Convert the number to a string and write it to the file
        # `write()` expects a string, so we convert the number to a string
        f.write(str(number))  # Write the number as a string to the file

# Main program execution
num = readNumber()  # Read the current number (how many times the program has been run)
num += 1  # Increment the number by 1 (since we're running the program one more time)
# Print a message showing how many times the program has been run using string formatting
print("We have run this program {} times".format(num))

# Write the updated number back to the file (save the new count)
writeNumber(num)
