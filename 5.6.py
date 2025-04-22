# List of temperatures in Fahrenheit
fahrenheit_temps = [32, 50, 77, 104, 212]

# Convert to Celsius using list comprehension
celsius_temps = [(temp - 32) * 5/9 for temp in fahrenheit_temps]

# Print the Celsius temperatures
print(celsius_temps)
