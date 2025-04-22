import random

# Generate 5 random odd integers
odd_integers = [random.choice(range(1, 101, 2)) for _ in range(5)]  # Odd numbers in the range 1 to 100
print("List of 5 random odd integers:", odd_integers)

# Generate 4 random even integers
even_integers = [random.choice(range(2, 101, 2)) for _ in range(4)]  # Even numbers in the range 2 to 100
print("List of 4 random even integers:", even_integers)

# Replace the third element of odd_integers with even_integers
odd_integers[2] = even_integers
print("\nList after replacing the third element with the list of even integers:", odd_integers)

# Flatten the list (handle the nested list in odd_integers[2])
flattened_list = []
for item in odd_integers:
    if isinstance(item, list):
        flattened_list.extend(item)  # If the item is a list, extend the flattened list with its contents
    else:
        flattened_list.append(item)

print("\nFlattened list:", flattened_list)

# Sort the flattened list
flattened_list.sort()
print("\nSorted flattened list:", flattened_list)
