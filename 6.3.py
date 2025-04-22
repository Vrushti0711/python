from datetime import date

# Two date tuples (day, month, year)
date1 = (10, 3, 2024)
date2 = (22, 4, 2025)

# Convert tuples to date objects
d1 = date(date1[2], date1[1], date1[0])  # (year, month, day)
d2 = date(date2[2], date2[1], date2[0])

# Calculate difference in days
difference = abs((d2 - d1).days)

# Print result
print(f"Number of days between {date1} and {date2}: {difference} days")
