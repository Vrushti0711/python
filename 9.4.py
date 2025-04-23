def reverse_list(lst):
    # Base case: if the list is empty or has one element, it is already reversed
    if len(lst) <= 1:
        return lst
    # Recursive case: reverse the rest of the list and append the first element at the end
    return reverse_list(lst[1:]) + [lst[0]]

# Example usage:
numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_list(numbers)
print("Reversed List:", reversed_numbers)
