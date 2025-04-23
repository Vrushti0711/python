class Weather:
    def __init__(self, parameters):
        # Store weather parameters in a list
        self.parameters = parameters

    def __contains__(self, item):
        # Overload 'in' operator to check if item is in the parameters list
        return item in self.parameters

# Example usage:
weather_today = Weather(["rainy", "windy", "cloudy"])

print("rainy" in weather_today)   # Output: True
print("sunny" in weather_today)   # Output: False
