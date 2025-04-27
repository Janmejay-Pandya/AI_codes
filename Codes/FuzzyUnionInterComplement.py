# Define fuzzy set operations

def fuzzy_union(set1, set2):
    return {x: max(set1.get(x, 0), set2.get(x, 0)) for x in set1.keys() | set2.keys()}

def fuzzy_intersection(set1, set2):
    return {x: min(set1.get(x, 0), set2.get(x, 0)) for x in set1.keys() | set2.keys()}

def fuzzy_complement(fuzzy_set):
    return {x: round(1 - v, 2) for x, v in fuzzy_set.items()}

# Define 3 fuzzy sets
A = {'x1': 0.1, 'x2': 0.5, 'x3': 0.9}
B = {'x1': 0.7, 'x2': 0.4, 'x3': 0.3}
C = {'x1': 0.2, 'x2': 0.8, 'x3': 0.6}

# Perform operations
print("Fuzzy Set A:", A)
print("Fuzzy Set B:", B)
print("Fuzzy Set C:", C)

# Union
union_AB = fuzzy_union(A, B)
print("\nUnion of A and B:", union_AB)

union_BC = fuzzy_union(B, C)
print("Union of B and C:", union_BC)

# Intersection
intersection_AB = fuzzy_intersection(A, B)
print("\nIntersection of A and B:", intersection_AB)

intersection_BC = fuzzy_intersection(B, C)
print("Intersection of B and C:", intersection_BC)

# Complement
complement_A = fuzzy_complement(A)
print("\nComplement of A:", complement_A)

complement_C = fuzzy_complement(C)
print("Complement of C:", complement_C)
