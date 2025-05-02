#WHILE LOOP ALLOWS YOU TO CONTINUE TO EXECUTE  A BLOCK OF CODE WHILE A CONDITION IS TRUE. ONCE THE CONDITION BECOMES FALSE THE LOOP STOPS EXECTURING        

age = int(input(" Please enter your age: "))

while (age < 20):
    print(" This person is younger than 20")
    age = int(input('Please enter your age again: '))
print('This person is old enough to enter')