import math

def generate_pythagorean_triplets(limit):
    triplets = []
    
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):  # Start from 'a' to avoid duplicates (e.g., (3,4) and (4,3))
            c = math.sqrt(a*2 + b*2)
            if c.is_integer() and c <= limit:
                triplets.append((a, b, int(c)))
    
    return triplets

# Limit set to 30
limit = 30
triplets = generate_pythagorean_triplets(limit)

# Output the Pythagorean triplets
for triplet in triplets:
    print(triplet)
