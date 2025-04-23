def count_lower_upper(s):
    # Initialize counters for lowercase and uppercase letters
    lower_count = 0
    upper_count = 0
    
    # Loop through each character in the string
    for char in s:
        # Check if the character is lowercase
        if char.islower():
            lower_count += 1
        # Check if the character is uppercase
        elif char.isupper():
            upper_count += 1
    
    # Return a dictionary with the counts of lowercase and uppercase letters
    return {'lowercase': lower_count, 'uppercase': upper_count}

# Example usage:
sample_string = "Hello World!"
result = count_lower_upper(sample_string)
print(result)
