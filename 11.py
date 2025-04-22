while True:
    try:
        # Ask user to input an integer
        num = int(input("Enter an integer: "))
        print(f"You entered the integer: {num}")
        break  # Exit the loop if input is valid
    except ValueError:
        # Handle the error if input is not an integer
        print("Error: That was not an integer. Please try again.")
