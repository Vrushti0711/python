# List of faculty names
faculty_names = ['John', 'Matthew', 'Elizabeth', 'Sophia', 'Alexander', 'Jake', 'Maximilian', 'Grace']

# Filter the names with more than 8 characters
filtered_names = [name for name in faculty_names if len(name) > 8]

# Print the filtered names
print("Faculty members with names longer than 8 characters:")
for name in filtered_names:
    print(name)
