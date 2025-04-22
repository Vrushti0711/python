# Define the two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Use list comprehension to create the third list
list3 = [num for num in list1 if num not in list2]

# Print the third list
print(list3)
