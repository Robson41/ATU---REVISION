'''1. Create a function without a return value:

Write a function called greet_user(name) that:
Takes a user's name as input
Prints: "Hello, <name>!"
Example call: greet_user("Mark")
Expected output: Hello, Mark!'''

def greet_user():
    name = input("Please enter your name: ")
    print(f'Hello, {name}!')


greet_user()


