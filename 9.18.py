def convert(s):
    # Split the string into words
    words = s.split()
    
    # Use set to remove duplicates
    unique_words = set(words)
    
    # Sort the words alphanumerically
    sorted_words = sorted(unique_words)
    
    # Join the sorted words back into a string
    return ' '.join(sorted_words)

# Example usage:
input_string = input("Enter a whitespace-separated string: ")

result = convert(input_string)
print("Result after removing duplicates and sorting:")
print(result)
