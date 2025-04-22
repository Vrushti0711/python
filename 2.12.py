import math

# Accept the coordinates of the center of the circle and the radius
cx, cy = map(float, input("Enter the center coordinates of the circle (cx, cy): ").split())
r = float(input("Enter the radius of the circle: "))

# Accept the coordinates of the point
px, py = map(float, input("Enter the coordinates of the point (px, py): ").split())

# Calculate the distance from the point to the center of the circle
distance = math.sqrt(math.pow(px - cx, 2) + math.pow(py - cy, 2))

# Check the position of the point relative to the circle
if distance < r:
    print("The point is inside the circle.")
elif distance == r:
    print("The point is on the circle.")
else:
    print("The point is outside the circle.")
