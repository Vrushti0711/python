# Convert bytes into KB, MB, and GB
bytes_value = 10485760  # Example: 10 MB

kilobytes = bytes_value / 1024
megabytes = bytes_value / (1024 ** 2)
gigabytes = bytes_value / (1024 ** 3)

print(f"{bytes_value} bytes is equal to:")
print(f"{kilobytes} KB")
print(f"{megabytes} MB")
print(f"{gigabytes} GB")
