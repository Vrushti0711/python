class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        # Overload the == operator to compare date values
        if isinstance(other, Date):
            return self.date == other.date
        return False

    def __str__(self):
        # Nicely format the date for printing
        return f"{self.date[0]:02d}-{self.date[1]:02d}-{self.date[2]}"

# Example usage:
date1 = Date(23, 4, 2025)
date2 = Date(23, 4, 2025)
date3 = Date(1, 1, 2024)

print(date1 == date2)  # Output: True
print(date1 == date3)  # Output: False
