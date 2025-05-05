# Import the os.path module to work with file and directory paths
import os.path

# Define the filename that will be checked
FILENAME = "count.txt"

# Check if the file does not exist using os.path.isfile
# os.path.isfile() returns True if the file exists and is a regular file, else it returns False
if not os.path.isfile(FILENAME):
    # If the file does not exist, print a message to the user
    print("File does not exist")
    # Initialize the file here if needed, for example:
    # with open(FILENAME, "w") as f:
    #     f.write("0")  # You can initialize the file with a default value
