# List of tuples: (roll number, name, age)
students = [
    (101, "Alice", 20),
    (102, "Bob", 21),
    (103, "Charlie", 19),
    (104, "Diana", 22),
    (105, "Ethan", 20)
]

# Separate lists for roll numbers, names, and ages
roll_nos = [student[0] for student in students]
names = [student[1] for student in students]
ages = [student[2] for student in students]

# Print the results
print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)
