# Original set of names
names_set = {"Alice", "Bob", "Anita", "Brian", "Amit", "Brenda"}

# Sets to store names starting with 'A' and 'B'
a_names = set()
b_names = set()

# Separate the names
for name in names_set:
    if name.startswith("A"):
        a_names.add(name)
    elif name.startswith("B"):
        b_names.add(name)

# Print the results
print("Names starting with A:", a_names)
print("Names starting with B:", b_names)
