# Define the filename where the number of program runs will be stored
FILENAME = "count.txt"

# Function to read the current count from the file
def readNumber():
    try:
        # Attempt to open the file in read mode and read its contents
        with open(FILENAME) as f:
            # Convert the contents of the file to an integer and return it
            number = int(f.read())
            return number
    except IOError:
        # If the file doesn't exist (first time running or file error), handle the error
        # We assume the program is running for the first time, so we return 0 (no previous runs)
        return 0
    

# Function to write the updated count to the file
def writeNumber(number):
    # Open the file in write mode ('wt' for text writing)
    with open(FILENAME, "wt") as f:
        # Write the number to the file. We need to convert the number to a string first
        f.write(str(number)) 

# Main execution starts here
# Read the current number of program runs
num = readNumber()

# Increment the number by 1 to count the current run
num += 1

# Print the number of times the program has been run
print ("we have run this program {} times".format(num))

# Write the updated count back to the file
writeNumber(num)
