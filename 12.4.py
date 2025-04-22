import math

class RegularShape:
    def _init_(self):
        self.shape = None

    def input_data(self):
        print("Choose a shape:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Equilateral Triangle")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            self.shape = 'square'
            self.side = float(input("Enter the side length of the square: "))
        elif choice == '2':
            self.shape = 'rectangle'
            self.length = float(input("Enter the length of the rectangle: "))
            self.breadth = float(input("Enter the breadth of the rectangle: "))
        elif choice == '3':
            self.shape = 'circle'
            self.radius = float(input("Enter the radius of the circle: "))
        elif choice == '4':
            self.shape = 'triangle'
            self.side = float(input("Enter the side length of the equilateral triangle: "))
        else:
            print("Invalid choice.")
            return False
        return True

    def perimeter(self):
        if self.shape == 'square':
            return 4 * self.side
        elif self.shape == 'rectangle':
            return 2 * (self.length + self.breadth)
        elif self.shape == 'circle':
            return 2 * math.pi * self.radius
        elif self.shape == 'triangle':
            return 3 * self.side

    def area(self):
        if self.shape == 'square':
            return self.side ** 2
        elif self.shape == 'rectangle':
            return self.length * self.breadth
        elif self.shape == 'circle':
            return math.pi * self.radius ** 2
        elif self.shape == 'triangle':
            return (math.sqrt(3) / 4) * self.side ** 2

# Example usage
shape = RegularShape()
if shape.input_data():
    print(f"\nPerimeter/Circumference: {shape.perimeter():.2f}")
    print(f"Area: {shape.area():.2f}")
