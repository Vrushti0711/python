# List containing strings and an integer
lst = ['madam', 'Python', 'malayalam', 12321]

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Ensure the item is a string and check if it is the same when reversed
    if isinstance(s, str):
        return s == s[::-1]
    return False

# Iterate through the list and print palindromes
for item in lst:
    if is_palindrome(str(item)):  # Convert non-strings to strings
        print(f"'{item}' is a palindrome.")
