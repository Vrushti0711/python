# Dictionary containing grocery items and their prices
prices = {
    "Apple": 30,
    "Banana": 15,
    "Milk": 40,
    "Bread": 25,
    "Mango": 60
}

# Dictionary containing grocery items and their quantity purchased
quantities = {
    "Apple": 3,
    "Banana": 6,
    "Milk": 2,
    "Bread": 1,
    "Mango": 12
}

# Initialize total bill
total_bill = 0

# Compute the total bill
for item in prices:
    # Calculate the total cost for the item (price * quantity)
    total_bill += prices[item] * quantities.get(item, 0)

# Print the total bill
print(f"Total Bill: Rs. {total_bill}")
