# Function to generate Fibonacci series
def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Input the number N
N = int(input("Enter the number N: "))

# Generate and print the Fibonacci series
fib_series = fibonacci(N)
print(f"The first {N} numbers of the Fibonacci series are:")
print(fib_series)
