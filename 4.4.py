# Check if the number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Check if the number is perfect
def is_perfect(num):
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

# Check if the number is an Armstrong number
def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    return sum(int(digit) ** num_len for digit in num_str) == num

# Check if the number is palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Check if the number is automorphic
def is_automorphic(num):
    square = num * num
    return str(square).endswith(str(num))

# Input number from user
num = int(input("Enter a number: "))

# Check for all properties
print(f"Is {num} prime? {'Yes' if is_prime(num) else 'No'}")
print(f"Is {num} perfect? {'Yes' if is_perfect(num) else 'No'}")
print(f"Is {num} Armstrong? {'Yes' if is_armstrong(num) else 'No'}")
print(f"Is {num} palindrome? {'Yes' if is_palindrome(num) else 'No'}")
print(f"Is {num} automorphic? {'Yes' if is_automorphic(num) else 'No'}")
