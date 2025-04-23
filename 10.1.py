import pandas as pd

# Function to read Excel file and convert to dictionary with total calculation
def read_and_convert_excel(file_path):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Initialize an empty dictionary to store student records
    student_dict = {}

    # Loop through each row in the DataFrame to create the dictionary
    for index, row in df.iterrows():
        rollno = row['rollno']
        name = row['name']
        marks1 = row['marks1']
        marks2 = row['marks2']
        marks3 = row['marks3']
        
        # Calculate the total marks
        total = marks1 + marks2 + marks3
        
        # Store the data in the dictionary
        student_dict[rollno] = {
            'name': name,
            'marks1': marks1,
            'marks2': marks2,
            'marks3': marks3,
            'total': total
        }

    return student_dict

# Example usage
file_path = 'students_data.xlsx'  # Provide the path to your Excel file here
student_data = read_and_convert_excel(file_path)

# Display the dictionary
print("Student Data:")
for rollno, data in student_data.items():
    print(f"Roll No: {rollno}, Name: {data['name']}, Marks: {data['marks1']}, {data['marks2']}, {data['marks3']}, Total: {data['total']}")
