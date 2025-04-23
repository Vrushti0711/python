def sanitize_list(lst, index=0):
    # Base case: If index exceeds the list length, return the list
    if index == len(lst):
        return lst
    
    # If the current element is negative, replace it with 0
    if lst[index] < 0:
        lst[index] = 0
    
    # Recursive call for the next index
    return sanitize_list(lst, index + 1)

# Example usage:
numbers = [10, -5, 3, -2, 8, -7]
sanitized_list = sanitize_list(numbers)
print("Sanitized List:", sanitized_list)
