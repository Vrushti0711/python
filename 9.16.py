def create_tuple_list(end_value):
    # Using list comprehension to create the list of tuples
    return [(x, x**2, x**3) for x in range(1, end_value + 1)]

# Example usage:
end_value = int(input("Enter the ending value: "))
result = create_tuple_list(end_value)

# Print the result
print("List of tuples:")
for item in result:
    print(item)
