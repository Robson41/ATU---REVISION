import sys  # Import the sys module to access command-line arguments

#print (sys.argv)  # This line is commented out, but it's used to print all command-line arguments

try:
    filename = sys.argv[1]  # Try to get the filename from the command-line arguments
    print(filename)  # Print the filename to confirm it's been received

    with open(filename) as fp:  # Open the file with the name from the command-line argument
        print(fp.read())  # Read and print the contents of the file

except IndexError as ie:  # Catch if there is an IndexError (if no argument is passed)
    print("please enter the filename as an argument")  # Notify the user to provide the filename
    #print(ie)  # This line is commented out; it would print the error message from the exception

except FileNotFoundError:  # Catch if the specified file is not found
    print(f"file {filename} not found, please enter a filename that exists")  # Notify the user that the file doesn't exist

