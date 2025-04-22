# Step 1: Create an empty set
names = set()

# Step 2: Add five new names
names.update(["Alice", "Bob", "Charlie", "Diana", "Ethan"])
print("After adding 5 names:", names)

# Step 3: Modify one existing name (e.g., change 'Charlie' to 'Carlos')
# Since sets are unordered and don't support item modification,
# we remove 'Charlie' and add 'Carlos'
if "Charlie" in names:
    names.remove("Charlie")
    names.add("Carlos")
print("After modifying 'Charlie' to 'Carlos':", names)

# Step 4: Delete two names (e.g., 'Bob' and 'Ethan')
names.discard("Bob")
names.discard("Ethan")
print("After deleting 'Bob' and 'Ethan':", names)
