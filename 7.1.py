# Creating three dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}

# Create an empty dictionary to store the result
dict4 = {}

# Update dict4 with the contents of dict1, dict2, and dict3
dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)

# Print the concatenated dictionary
print("Concatenated Dictionary:", dict4)
