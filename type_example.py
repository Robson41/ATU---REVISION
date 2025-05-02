number = 12
print(f'The current type for number is {type(number)}')

convert_to_string = str(number)
print(f'After the conversion of {number}, the current type for number is {type(convert_to_string)}')

print(f' the type of type is the class type because all types in Python (like str, int, etc.) are themselves objects of the type class, therefore the type of the type from the integer type is {type(type(number))} and the type from the string type is {type(type(convert_to_string))}' )