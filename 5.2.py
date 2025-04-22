import random

# Generate 20 random integers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(20)]

# Accept a number from the user
user_number = int(input("Enter a number to find its positions in the list: "))

# Find all occurrences of the number and their positions
positions = [index for index, value in enumerate(random_numbers) if value == user_number]

# Print the results
if positions:
    print(f"The number {user_number} occurs at the following positions: {positions}")
else:
    print(f"The number {user_number} does not occur in the list.")
