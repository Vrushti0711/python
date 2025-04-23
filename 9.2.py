def decimal_to_binary(n):
    # Base case: when n is 0, return an empty string
    if n == 0:
        return ""
    
    # Recursive case: divide n by 2 and prepend the result of n % 2
    return decimal_to_binary(n // 2) + str(n % 2)

# Example usage:
number = int(input("Enter a positive integer: "))
# Special case for 0, as its binary equivalent is "0"
if number == 0:
    print("Binary equivalent: 0")
else:
    print("Binary equivalent:", decimal_to_binary(number))
