# This function returns an empty list, representing the modules a student is enrolled in.
# It’s a placeholder for now — you could expand it later to allow module input.
def readModules():
    return []

# This function adds a student to the list of students.
def doAdd(students):
    # Create an empty dictionary to hold the current student's data.
    currentStudent = {}
    
    # Prompt the user to enter the student's name and store it in the dictionary.
    currentStudent["name"] = input("enter name :")
    
    # Assign the output of readModules (currently an empty list) to the student's "modules".
    currentStudent["modules"] = readModules()
    
    # Add the current student dictionary to the students list.
    students.append(currentStudent)


# ---------- TESTING THE FUNCTIONALITY ----------§
# Create an empty list to store all students.
students = []

# Call the doAdd function twice to add two students to the list.
doAdd(students)
doAdd(students)

# Print out the list of student dictionaries.
print(students)

'''What This Code Does:
It builds a list of student dictionaries.
Each dictionary contains the student's name and an empty list of modules.
It demonstrates use of functions, dictionaries, lists, and user input.'''