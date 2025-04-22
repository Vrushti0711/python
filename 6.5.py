# List with some empty tuples
tuple_list = [(), (1, 2), (), (3, 4, 5), (), (6,)]

# Remove empty tuples using list comprehension
filtered_list = [t for t in tuple_list if t]

# Print the result
print("Original list:", tuple_list)
print("Filtered list (without empty tuples):", filtered_list)
