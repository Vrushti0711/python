# Function to remove one string from another string
def remove_substring(main_string, sub_string):
    # Find the position of sub_string in main_string
    start = -1
    for i in range(len(main_string) - len(sub_string) + 1):
        if main_string[i:i + len(sub_string)] == sub_string:
            start = i
            break
    
    # If substring is found, remove it
    if start != -1:
        # Construct the final string by removing the substring
        final_string = main_string[:start] + main_string[start + len(sub_string):]
        return final_string
    else:
        return main_string  # If substring is not found, return the original string

# Accept the strings from the user
onestring = input("Enter the main string: ")
removestring = input("Enter the string to remove: ")

# Call the function and print the result
finalstring = remove_substring(onestring, removestring)
print(f"The final string is: {finalstring}")
