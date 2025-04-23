# Define the functions
def fun():
    print("This is the fun() function.")

def disp():
    print("This is the disp() function.")

def msg():
    print("This is the msg() function.")

# Store the functions in a list
functions = [fun, disp, msg]

# Loop through the list and call each function
for func in functions:
    func()
