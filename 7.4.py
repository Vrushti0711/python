# Read a string from the user
input_string = input("Enter a string: ")

# Initialize an empty dictionary to store frequency of characters
char_frequency = {}

# Loop through each character in the string
for char in input_string:
    if char in char_frequency:
        char_frequency[char] += 1  # Increment the count of the character
    else:
        char_frequency[char] = 1  # Initialize the count for the new character

# Print the dictionary containing character frequencies
print("Character frequencies:", char_frequency)
