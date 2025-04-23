def sum_list(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: sum the first element and the sum of the rest of the list
    return lst[0] + sum_list(lst[1:])

def average(lst):
    # Base case: if the list is empty, return 0 (to avoid division by zero)
    if not lst:
        return 0
    # Get the sum and the length of the list, then calculate the average
    total_sum = sum_list(lst)
    return total_sum / len(lst)

# Example usage:
numbers = [10, 20, 30, 40, 50]
avg = average(numbers)
print(f"The average of the list is: {avg}")
