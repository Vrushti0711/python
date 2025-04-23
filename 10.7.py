import pickle

# Define the Employee class
class Employee:
    def __init__(self, empcode, empname, date_of_joining, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = date_of_joining
        self.salary = salary

    def display(self):
        print("Employee Code:", self.empcode)
        print("Employee Name:", self.empname)
        print("Date of Joining:", self.date_of_joining)
        print("Salary:", self.salary)

# Create an Employee object
emp = Employee("E101", "Alice Johnson", "2021-06-15", 75000)

# Serialize the object to a file
with open("employee.dat", "wb") as f:
    pickle.dump(emp, f)
    print("Employee object serialized to 'employee.dat'")

# Deserialize the object from the file
with open("employee.dat", "rb") as f:
    loaded_emp = pickle.load(f)
    print("\nEmployee object deserialized from 'employee.dat':\n")
    loaded_emp.display()
