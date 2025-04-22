import random

# Generate 30 random numbers between -100 and 100
random_numbers = [random.randint(-100, 100) for _ in range(30)]

# Create lists for positive and negative numbers
positive_numbers = [num for num in random_numbers if num > 0]
negative_numbers = [num for num in random_numbers if num < 0]

# Print the lists
print("Random Numbers:", random_numbers)
print("Positive Numbers:", positive_numbers)
print("Negative Numbers:", negative_numbers)
