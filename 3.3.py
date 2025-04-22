# Function to check if one string is in another
def is_substring(str1, str2):
    # Loop through each character in str1 and try to match it with str2
    for i in range(len(str2) - len(str1) + 1):
        # Check if the substring starting at position i in str2 matches str1
        if str2[i:i + len(str1)] == str1:
            return True
    return False

# Accept two strings from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check if str1 is a substring of str2
if is_substring(str1, str2):
    print(f"'{str1}' is present in '{str2}'.")
else:
    print(f"'{str1}' is not present in '{str2}'.")
