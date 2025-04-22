def count_alphabets_and_digits(input_string):
    alphabets = 0
    digits = 0
    
    for char in input_string:
        if char.isalpha():  # Check if the character is an alphabet
            alphabets += 1
        elif char.isdigit():  # Check if the character is a digit
            digits += 1
    
    print(f"Number of Alphabets: {alphabets}")
    print(f"Number of Digits: {digits}")

# Input string from user
input_string = input("Enter a string: ")
count_alphabets_and_digits(input_string)
