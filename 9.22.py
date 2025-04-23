# Define the two lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]

# Use map and lambda to add corresponding elements from both lists
result = list(map(lambda x, y: x + y, list1, list2))

# Print the result
print("List with corresponding elements added:", result)
