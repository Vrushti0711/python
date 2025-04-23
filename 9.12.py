def compute(n):
    # Create the values of nn, nnn, and nnnn
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    nnnn = int(str(n) * 4)
    
    # Calculate the sum of n, nn, nnn, and nnnn
    result = n + nn + nnn + nnnn
    return result

# Test the function for digits 4 to 7
for digit in range(4, 8):
    result = compute(digit)
    print(f"compute({digit}) = {result}")
