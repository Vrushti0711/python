import math

class Solid:
    def _init_(self):
        self.shape = None

    def input_data(self):
        print("Choose a solid to calculate:")
        print("1. Cube")
        print("2. Sphere")
        print("3. Cylinder")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            self.shape = 'cube'
            self.side = float(input("Enter the side length of the cube: "))
        elif choice == '2':
            self.shape = 'sphere'
            self.radius = float(input("Enter the radius of the sphere: "))
        elif choice == '3':
            self.shape = 'cylinder'
            self.radius = float(input("Enter the radius of the cylinder: "))
            self.height = float(input("Enter the height of the cylinder: "))
        else:
            print("Invalid choice.")
            return False
        return True

    def surface_area(self):
        if self.shape == 'cube':
            return 6 * self.side ** 2
        elif self.shape == 'sphere':
            return 4 * math.pi * self.radius ** 2
        elif self.shape == 'cylinder':
            return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        if self.shape == 'cube':
            return self.side ** 3
        elif self.shape == 'sphere':
            return (4/3) * math.pi * self.radius ** 3
        elif self.shape == 'cylinder':
            return math.pi * self.radius ** 2 * self.height

# Example usage
solid = Solid()
if solid.input_data():
    print(f"\nSurface Area: {solid.surface_area():.2f}")
    print(f"Volume: {solid.volume():.2f}")
