# Accept the coordinates of the three points
x1, y1 = map(float, input("Enter the coordinates of point 1 (x1, y1): ").split())
x2, y2 = map(float, input("Enter the coordinates of point 2 (x2, y2): ").split())
x3, y3 = map(float, input("Enter the coordinates of point 3 (x3, y3): ").split())

# Check if the slopes between points (x1, y1), (x2, y2) and (x2, y2), (x3, y3) are equal
# This is equivalent to checking if the cross product is zero
if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
    print("The three points are collinear.")
else:
    print("The three points are not collinear.")
