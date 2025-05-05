# Initialize an empty list to store prime numbers
primes = []

# Define the upper limit for checking primes
upto = 100000

# Loop through all candidate numbers starting from 2 (the first prime number)
for candidate in range(2, upto):
    
    # Assume the current candidate is prime until proven otherwise
    isPrime = True

    # Only check divisibility against previously found primes (optimization)
    for divisor in primes:
        
        # If the candidate is divisible by any earlier prime, it's not a prime
        if (candidate % divisor == 0):
            isPrime = False  # Mark it as not a prime
            break            # Exit the loop early — no need to check further

    # If it's still marked as prime after all checks, add it to the list
    if isPrime:
        primes.append(candidate)

# Print the full list of prime numbers found up to 100,000
print(primes)
