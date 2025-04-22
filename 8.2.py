import random

# Step 1: Create a set of 10 random numbers in the range 15 to 45
random_numbers = set(random.sample(range(15, 46), 10))
print("Original set:", random_numbers)

# Step 2: Count how many numbers are less than 30
less_than_30 = [num for num in random_numbers if num < 30]
print("Numbers less than 30:", less_than_30)
print("Count:", len(less_than_30))

# Step 3: Delete all numbers greater than 35
filtered_set = {num for num in random_numbers if num <= 35}
print("Set after deleting numbers greater than 35:", filtered_set)
