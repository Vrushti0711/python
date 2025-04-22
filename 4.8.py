# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Input a number from the user
num = int(input("Enter a number: "))

# Calculate and print the factorial
print(f"The factorial of {num} is {factorial(num)}")
