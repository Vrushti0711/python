# Dictionary to map numbers to words
num_to_word = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
}

# Accept a number from the user
num = int(input("Enter a number between 0 and 19: "))

# Check if the number is within the valid range
if 0 <= num <= 19:
    print(f"The number {num} in words is: {num_to_word[num]}")
else:
    print("Please enter a number between 0 and 19.")
