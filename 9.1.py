def prime_factors(n, divisor=2):
    # Base case: if n is 1, return an empty list (no more prime factors)
    if n == 1:
        return []
    
    # If n is divisible by divisor, it's a prime factor
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    
    # If not divisible, check the next potential divisor
    return prime_factors(n, divisor + 1)

# Example usage:
number = int(input("Enter a positive integer: "))
factors = prime_factors(number)
print(f"Prime factors of {number}: {factors}")
