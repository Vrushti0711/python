#Accept a string from the user
input_string = input("Enter a string: ")

# Vowels to check
vowels = "aeiouAEIOU"

# Initialize a counter for vowels
vowel_count = 0

# Loop through each character in the string
for char in input_string:
    if char in vowels:
        vowel_count += 1

# Print the number of vowels
print(f"The number of vowels in the string is: {vowel_count}")
