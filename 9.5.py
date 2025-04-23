def power(**kwargs):
    # Extracting 'a' and 'b' from the keyword arguments
    a = kwargs.get('a')
    b = kwargs.get('b')

    # Base case: when b is 0, a^0 = 1 (any number raised to the power of 0 is 1)
    if b == 0:
        return 1
    # If b is positive, multiply a with recursive call
    elif b > 0:
        return a * power(a=a, b=b-1)
    # If b is negative, calculate the reciprocal of a^(-b)
    else:
        return 1 / power(a=a, b=-b)

# Example usage:
result = power(a=2, b=3)
print("2^3 =", result)

result_neg = power(a=2, b=-3)
print("2^-3 =", result_neg)
