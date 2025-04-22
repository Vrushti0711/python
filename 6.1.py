# List containing names of boys (as tuples) and girls (as strings)
people = ["Anita", ("Rohit",), "Priya", ("Aman",), "Sneha", ("Vikram",), "Kiran"]

# Initialize counters
boys = 0
girls = 0

# Count boys and girls
for person in people:
    if isinstance(person, tuple):
        boys += 1
    else:
        girls += 1

# Print the results
print("Number of boys:", boys)
print("Number of girls:", girls)
