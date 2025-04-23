def ispangram(s):
    # Define the set of all alphabets
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    
    # Convert the string to lowercase and create a set of characters in the string
    s_set = set(s.lower())
    
    # Remove any non-alphabet characters from the set
    s_set = {char for char in s_set if char.isalpha()}
    
    # Check if the alphabet set is a subset of the characters in the string
    return alphabet_set <= s_set

# Example usage:
input_string = input("Enter a string: ")

# Test the function with the user's input
if ispangram(input_string):
    print("The given string is a pangram.")
else:
    print("The given string is not a pangram.")
