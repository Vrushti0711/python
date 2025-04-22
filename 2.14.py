# Function to assign grade based on marks
def assign_grade(marks):
    if marks == "Absent":
        return "NA"
    elif marks <= 39:
        return "F"
    elif marks <= 44:
        return "P"
    elif marks <= 49:
        return "C"
    elif marks <= 54:
        return "B"
    elif marks <= 59:
        return "B+"
    elif marks <= 69:
        return "A"
    elif marks <= 79:
        return "A+"
    elif marks <= 100:
        return "O"

# Accept marks for three subjects
marks1 = input("Enter marks for subject 1 (or 'Absent' if not attended): ")
if marks1 != "Absent":
    marks1 = int(marks1)

marks2 = input("Enter marks for subject 2 (or 'Absent' if not attended): ")
if marks2 != "Absent":
    marks2 = int(marks2)

marks3 = input("Enter marks for subject 3 (or 'Absent' if not attended): ")
if marks3 != "Absent":
    marks3 = int(marks3)

# Check for fail condition (if any mark is <= 39, consider fail)
if (marks1 == "Absent" or marks2 == "Absent" or marks3 == "Absent" or 
    (marks1 <= 39 and marks1 != "Absent") or 
    (marks2 <= 39 and marks2 != "Absent") or 
    (marks3 <= 39 and marks3 != "Absent")):
    status = "Fail"
else:
    status = "Pass"

# Calculate total and average if all marks are available
if marks1 != "Absent" and marks2 != "Absent" and marks3 != "Absent":
    total = marks1 + marks2 + marks3
    average = total / 3
else:
    total = average = "N/A"  # If any subject is Absent, set total/average to N/A

# Print the results
print("\nResults:")
if marks1 != "Absent":
    print(f"Subject 1: {marks1} - Grade: {assign_grade(marks1)}")
else:
    print(f"Subject 1: Absent - Grade: NA")

if marks2 != "Absent":
    print(f"Subject 2: {marks2} - Grade: {assign_grade(marks2)}")
else:
    print(f"Subject 2: Absent - Grade: NA")

if marks3 != "Absent":
    print(f"Subject 3: {marks3} - Grade: {assign_grade(marks3)}")
else:
    print(f"Subject 3: Absent - Grade: NA")

print(f"\nTotal Marks: {total}")
print(f"Average Marks: {average}")
print(f"Status: {status}")
