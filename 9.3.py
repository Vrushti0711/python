def count_vowels(s):
    # Base case: if the string is empty, return 0
    if len(s) == 0:
        return 0
    
    # If the first character is a vowel, count it and recurse for the rest of the string
    vowels = 'aeiouAEIOU'
    if s[0] in vowels:
        return 1 + count_vowels(s[1:])
    
    # Otherwise, just recurse for the rest of the string
    return count_vowels(s[1:])

# Example usage:
input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print(f"Number of vowels in the string: {vowel_count}")
