# Function to convert string to lowercase
def to_lower_case(input_string):
    result = ""
    for char in input_string:
        if 'A' <= char <= 'Z':  # Check if character is uppercase
            result += chr(ord(char) + 32)  # Convert to lowercase
        else:
            result += char  # If it's already lowercase or non-alphabet, keep it as it is
    return result

# Function to convert string to uppercase
def to_upper_case(input_string):
    result = ""
    for char in input_string:
        if 'a' <= char <= 'z':  # Check if character is lowercase
            result += chr(ord(char) - 32)  # Convert to uppercase
        else:
            result += char  # If it's already uppercase or non-alphabet, keep it as it is
    return result

# Function to toggle the case of each character in the string
def toggle_case(input_string):
    result = ""
    for char in input_string:
        if 'a' <= char <= 'z':  # Check if character is lowercase
            result += chr(ord(char) - 32)  # Convert to uppercase
        elif 'A' <= char <= 'Z':  # Check if character is uppercase
            result += chr(ord(char) + 32)  # Convert to lowercase
        else:
            result += char  # Non-alphabet characters remain the same
    return result

# Accept input string from the user
input_string = input("Enter a string: ")

# Convert to lowercase, uppercase, and toggle case
lower_case_string = to_lower_case(input_string)
upper_case_string = to_upper_case(input_string)
toggled_case_string = toggle_case(input_string)

# Print the results
print(f"Lowercase: {lower_case_string}")
print(f"Uppercase: {upper_case_string}")
print(f"Toggled case: {toggled_case_string}")
