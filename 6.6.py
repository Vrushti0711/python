#Original tuple
my_tuple = (10, 20, 30)

# Convert to list
temp_list = list(my_tuple)

# Modify an element
temp_list[1] = 99

# Convert back to tuple
my_tuple = tuple(temp_list)

# Print the modified tuple
print("Modified tuple:", my_tuple)
