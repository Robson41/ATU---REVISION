# Define the filename where the number will be stored
FILENAME = "count.txt"

# Define a function to write a number to a file
def writeNumber(number):
    # Open the file in write text mode ("wt") — this creates the file if it doesn't exist,
    # or overwrites it if it already does
    with open(FILENAME, "wt") as f:
        # The write() method requires a string, so we convert the number to a string
        f.write(str(number)) 

# Test the function by writing the number 0 to the file
writeNumber(0)
