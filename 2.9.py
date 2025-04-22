##Accept the length and breadth of the rectangle
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# Calculate the area and perimeter
area = length * breadth
perimeter = 2 * (length + breadth)

# Check if the area is greater than the perimeter
if area > perimeter:
    print("The area of the rectangle is greater than its perimeter.")
else:
    print("The perimeter of the rectangle is greater than or equal to its area.")
