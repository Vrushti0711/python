import math

# Function to calculate nCr
def nCr(n, r):
    return math.comb(n, r)

# Function to calculate nPr
def nPr(n, r):
    return math.perm(n, r)

# Input values for n and r
n = int(input("Enter n: "))
r = int(input("Enter r: "))

# Print nCr and nPr
print(f"nCr (Combinations) = {nCr(n, r)}")
print(f"nPr (Permutations) = {nPr(n, r)}")
