# Open the file "test-d.txt" in write mode ("w"). 
# If the file exists, it will be overwritten. If it doesn't exist, a new file will be created.
with open("test-d.txt", "w") as f:
    # Write the string "test d\n" into the file.
    # The write() method returns the number of characters written (including the newline character \n).
    data = f.write("test d\n") 
    # Print the number of characters written to the file.
    print(data)

# Open the same file "test-d.txt" again, but this time in append mode ("a").
# This allows new content to be added to the file without overwriting the existing content.
with open("test-d.txt", "a") as f2:
    # Write the string "another line" to the file.
    # Again, the write() method returns the number of characters written.
    data = f2.write("another line") 
    # Print the number of characters written to the file.
    print(data)
