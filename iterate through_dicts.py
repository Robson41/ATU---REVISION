# This program stores a student's name and their courses with grades using a dictionary.
# The goal is to print out the student's name and a list of their course names and grades.

# Creating a dictionary called 'student' that contains:
# - A string entry for "name"
# - A list of dictionaries under the key "modules", where each dictionary contains:
#   - courseName: the name of the course
#   - grade: the grade for that course
student = {
    "name": "Mary",  # The student's name
    "modules": [     # A list of dictionaries, each representing a module/course
        {
            "courseName": "Programming",  # First course
            "grade": 45                   # Grade for the first course
        },
        {
            "courseName": "History",     # Second course
            "grade": 99                  # Grade for the second course
        }
    ]
}

# Print the student's name using string formatting
print("Student: {}".format(student["name"]))

# Loop through the list of modules (courses) inside the student dictionary
for module in student["modules"]:
    # For each module (which is a dictionary), access its "courseName" and "grade"
    # Print them in a formatted way, with a tab character for neatness
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))
