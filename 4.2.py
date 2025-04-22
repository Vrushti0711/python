def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Input the number for the multiplication table
num = int(input("Enter a number: "))
multiplication_table(num)
