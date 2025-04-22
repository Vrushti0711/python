# List of tuples: (food item, price)
food_prices = [
    ("Pizza", 250),
    ("Burger", 120),
    ("Pasta", 180),
    ("Fries", 70),
    ("Sandwich", 90)
]

# Sort the list in descending order by price
sorted_food = sorted(food_prices, key=lambda x: x[1], reverse=True)

# Print the sorted list
print("Food items sorted by price (high to low):")
for item, price in sorted_food:
    print(f"{item}: Rs. {price}")
