# Define the filename that stores the number
FILENAME = "count.txt"

# Function to read a number from the file
def readNumber():
    # Open the file in read mode (default is "r")
    with open(FILENAME) as f:
        # Read the contents of the file and convert to an integer
        number = int(f.read())
        return number  # Return the integer value

# Call the function and store the result in variable 'num'
num = readNumber()

# Print the number read from the file
print(num)
