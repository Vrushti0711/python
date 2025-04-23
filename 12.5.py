class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize()

    def normalize(self):
        # Normalize seconds and minutes
        self.minutes += self.seconds // 60
        self.seconds = self.seconds % 60

        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def from_seconds(total_seconds):
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return Time(hours, minutes, seconds)

    def __add__(self, other):
        if isinstance(other, Time):
            total = self.to_seconds() + other.to_seconds()
            return Time.from_seconds(total)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Time):
            total = self.to_seconds() - other.to_seconds()
            if total < 0:
                raise ValueError("Negative time result is not allowed.")
            return Time.from_seconds(total)
        else:
            raise TypeError("Unsupported operand type for -")

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

# Example usage:
time1 = Time(2, 45, 50)
time2 = Time(1, 20, 30)

print("Time 1:", time1)           # Output: 02:45:50
print("Time 2:", time2)           # Output: 01:20:30

sum_time = time1 + time2
print("Sum:", sum_time)           # Output: 04:06:20

diff_time = time1 - time2
print("Difference:", diff_time)   # Output: 01:25:20
