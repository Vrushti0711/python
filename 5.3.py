import random

# Generate 50 random numbers in the range 1 to 30
random_numbers = [random.randint(1, 30) for _ in range(50)]

# Remove duplicates by converting the list to a set and then back to a list
unique_numbers = list(set(random_numbers))

# Print the original and the list with unique numbers
print("Random Numbers:", random_numbers)
print("Unique Numbers:", unique_numbers)
