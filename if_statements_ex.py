age = int(input('Please enter your age: '))

older = age + 7

if (age >= 9 and older >= 30):
    print('valid statement')

if (age >= 11 or older >=24):
    print('This one is a valid statement')

else: 
    print('invalid statement')