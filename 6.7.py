# Original tuple
my_tuple = (10, 20, 30, 40, 50)

# Let's say we want to delete the element at index 2 (value 30)
index_to_remove = 2

# Create a new tuple without the element at the specified index
new_tuple = my_tuple[:index_to_remove] + my_tuple[index_to_remove + 1:]

# Print the new tuple
print("Original tuple:", my_tuple)
print("Tuple after deleting element at index 2:", new_tuple)
