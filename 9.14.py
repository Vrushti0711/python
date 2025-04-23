def sum_avg(marks):
    # Calculate the total sum of marks
    total = sum(marks)
    # Calculate the average
    average = total / len(marks)
    return total, average

# Example usage:
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter the marks for subject {i}: "))
    marks.append(mark)

# Call the function to get total and average
total, average = sum_avg(marks)

# Output the result
print(f"Total Marks: {total}")
print(f"Average Marks: {average:.2f}")
