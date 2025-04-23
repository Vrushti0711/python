class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero complex number.")
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real, imag)

    def __str__(self):
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

# Example usage:
def main():
    print("Enter first complex number:")
    r1 = float(input("Real part: "))
    i1 = float(input("Imaginary part: "))
    c1 = ComplexNumber(r1, i1)

    print("Enter second complex number:")
    r2 = float(input("Real part: "))
    i2 = float(input("Imaginary part: "))
    c2 = ComplexNumber(r2, i2)

    print("\nResults:")
    print("Addition:       ", c1 + c2)
    print("Subtraction:    ", c1 - c2)
    print("Multiplication: ", c1 * c2)
    try:
        print("Division:       ", c1 / c2)
    except ZeroDivisionError as e:
        print("Division:       Error -", e)

if __name__ == "__main__":
    main()
