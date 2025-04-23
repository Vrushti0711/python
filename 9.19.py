def count_alpha_digits(s):
    result = {'alphabets': 0, 'digits': 0}
    
    for char in s:
        if char.isalpha():
            result['alphabets'] += 1
        elif char.isdigit():
            result['digits'] += 1

    return result

# Example usage
input_string = input("Enter a string: ")
counts = count_alpha_digits(input_string)

print("Counts:")
print("Alphabets:", counts['alphabets'])
print("Digits:", counts['digits'])
