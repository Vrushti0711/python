def ispalindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is the same when reversed
    return cleaned == cleaned[::-1]

# Example usage:
input_string = input("Enter a word or phrase: ")

if ispalindrome(input_string):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
