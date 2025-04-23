def string_length(s):
    # Base case: If the string is empty, return 0
    if s == "":
        return 0
    # Recursive case: Count 1 for the first character and process the rest of the string
    return 1 + string_length(s[1:])

# Example usage:
input_string = input("Enter a string: ")
length = string_length(input_string)
print(f"The length of the string is: {length}")
