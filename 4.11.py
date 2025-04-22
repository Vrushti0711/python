import math

# Function to calculate sin(x) using series expansion
def sin_series(x, terms=10):
    result = 0
    for n in range(terms):
        # Alternating sign
        sign = (-1) ** n
        # Calculate the term
        result += sign * (x**(2*n+1)) / math.factorial(2*n+1)
    return result

# Input the angle in degrees
x_degrees = float(input("Enter the angle in degrees: "))

# Convert degrees to radians
x_radians = x_degrees * math.pi / 180

# Calculate sin(x) using the series expansion
sin_value = sin_series(x_radians)

print(f"sin({x_degrees}) = {sin_value}")
