#Dictionary with department number as keys, and a list of tuples (employee roll no., salary)
dept_data = {
    101: [(1, 50000), (2, 60000), (3, 45000), (4, 70000)],  # Department 101
    102: [(5, 40000), (6, 55000), (7, 65000)],  # Department 102
    103: [(8, 75000), (9, 30000), (10, 85000)],  # Department 103
}

# Iterate over each department and find the min and max salary
for dept_no, employees in dept_data.items():
    # Extract the salary list for each department
    salaries = [salary for roll_no, salary in employees]
    
    # Find minimum and maximum salary
    min_salary = min(salaries)
    max_salary = max(salaries)
    
    # Print results
    print(f"Department {dept_no}:")
    print(f"  Minimum Salary: {min_salary}")
    print(f"  Maximum Salary: {max_salary}")
    print()
