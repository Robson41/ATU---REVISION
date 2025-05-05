import random  # Import the random module to generate random numbers

# Initialize an empty list to act as our queue
queue = []

# Set how many random numbers to generate
numberOfNumbers = 10

# Set the maximum possible value for a random number
rangeTo = 100

# Generate 10 random numbers between 0 and 100 and add them to the queue
for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))  # Add (append) each random number to the end of the list

# Print the full queue before we start removing values
print("queue is {}".format(queue))

# Loop as long as there are elements in the queue
while len(queue) != 0:
    
    # Remove the first item in the queue (FIFO behavior) and store it in currentNumber
    currentNumber = queue.pop(0)

    # Print the number that was just removed and the current state of the queue
    print("current Number is {} and the queue is {} ".format(currentNumber, queue))

# When all items are removed, notify that the queue is now empty
print("the queue is now empty")
