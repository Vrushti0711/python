def create_array(dim1, dim2, dim3, value):
    # Create a 3D array with the given dimensions (dim1, dim2, dim3)
    # Initialize all elements to the specified 'value'
    array = [[[value for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]
    
    return array

# Example usage:
dim1, dim2, dim3 = 3, 4, 5  # Dimensions of the 3D array (3x4x5)
initial_value = 7  # Initial value for each element in the 3D array

result_array = create_array(dim1, dim2, dim3, initial_value)

# Printing the 3D array
for layer in result_array:
    for row in layer:
        print(row)
    print()  # Print a blank line between layers for better readability
