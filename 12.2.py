class Matrix:
    def __init__(self, data=None):
        if data:
            if len(data) != 3 or any(len(row) != 3 for row in data):
                raise ValueError("Only 3x3 matrices are supported.")
            self.data = data
        else:
            self.data = [[0]*3 for _ in range(3)]

    def input_matrix(self):
        print("Enter the elements of a 3x3 matrix row by row:")
        for i in range(3):
            self.data[i] = list(map(int, input(f"Row {i+1}: ").split()))

    def display(self):
        for row in self.data:
            print(row)

    def add(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def multiply(self, other):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)

# Example usage
def main():
    print("Matrix A:")
    A = Matrix()
    A.input_matrix()

    print("\nMatrix B:")
    B = Matrix()
    B.input_matrix()

    print("\nMatrix A:")
    A.display()
    print("\nMatrix B:")
    B.display()

    print("\nA + B:")
    A.add(B).display()

    print("\nA x B:")
    A.multiply(B).display()

    print("\nTranspose of A:")
    A.transpose().display()

if __name__ == "__main__":
    main()
