import random

# Generate a list of 10 different random numbers between -15 and 15
random_numbers = random.sample(range(-15, 16), 10)

# Create a new list by squaring each number
squared_numbers = [num ** 2 for num in random_numbers]

# Print the results
print("Random Numbers:", random_numbers)
print("Squared Numbers:", squared_numbers)
