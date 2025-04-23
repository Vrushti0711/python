def create_list(list1, list2):
    # Using set intersection to find common elements
    return list(set(list1) & set(list2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

result = create_list(list1, list2)

print("Intersection of the two lists:", result)
