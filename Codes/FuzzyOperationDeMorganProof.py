""" Implement Fuzzy set operations  union, intersection and complement.
Demonstrate De Morgans Law ( Complement of Union) with 2 fuzzy sets."""

# def fuzzy_union(set1, set2):
#     return {x:max(set1.get(x,0),set2.get(x,0)) for x in set1.keys() | set2.keys()}

# def fuzzy_intersection(set1, set2):
#     return {x:min(set1.get(x,0),set2.get(x,0)) for x in set1.keys() | set2.keys()}

# def fuzzy_complement(fuzzy_set):
#     return {x:round(1-v,2) for x,v in fuzzy_set.items()}

# set1 = {'x1':0.1,'x2':0.5,'x3':0.9}
# set2 = {'x1':0.7,'x2':0.4,'x3':0.3}

# union_AB=fuzzy_union(set1,set2)
# print("Union of A and B:",union_AB)

# complement_Union_AB=fuzzy_complement(union_AB)
# print("\nComplement of Union of A and B:",complement_Union_AB)

# complement_A=fuzzy_complement(set1)
# complement_B=fuzzy_complement(set2)
# print("\nComplement of A:",complement_A)
# print("\nComplement of B:",complement_B)

# de_morgan_result=fuzzy_intersection(complement_A,complement_B)
# print("\nDe Morgan's Law Result (Complement of A and B):",de_morgan_result)

# are_equal= complement_Union_AB == de_morgan_result
# print("\nDe Morgan's Law holds:", are_equal)


# def fuzzy_union(set1,set2):
#     return {x:max(set1.get(x,0),set2.get(x,0)) for x in set1.keys()| set2.keys()}

# def fuzzy_intersection(set1,set2):
#     return {x:min(set1.get(x,0),set2.get(x,0)) for x in set1.keys()| set2.keys()}

# def fuzzy_complement(fuzzy_set):
#     return {x:round(1-v,2) for x,v in fuzzy_set.items()}

# def is_subset(set1,set2):
#     return all(set1.get(x,0)<=set2.get(x,0) for x in set1.keys())


# set1 = {'x1':0.1,'x2':0.5,'x3':0.9}
# set2 = {'x1':0.7,'x2':0.4,'x3':0.3}
# union_AB=fuzzy_union(set1,set2)
# print("Union of A and B:",union_AB)
# intersection_AB=fuzzy_intersection(set1,set2)
# print("\nIntersection of A and B:",intersection_AB)


def fuzzy_union(A, B):
    return {x: round(max(A.get(x, 0), B.get(x, 0)), 2) for x in set(A) | set(B)}

def fuzzy_intersection(A, B):
    return {x: round(min(A.get(x, 0), B.get(x, 0)), 2) for x in set(A) & set(B)}

def fuzzy_complement(A):
    return {x: round(1 - A[x], 2) for x in A}

def is_subset(A, B):
    return all(A.get(x, 0) <= B.get(x, 0) for x in A)

def de_morgan_check(A, B):
    return fuzzy_complement(fuzzy_union(A, B)) == fuzzy_intersection(fuzzy_complement(A), fuzzy_complement(B))

def get_fuzzy_set(name):
    n = int(input(f"Enter number of elements in fuzzy set {name}: "))
    fuzzy_set = {}
    for _ in range(n):
        key, value = input("Enter element (string) and membership value (space-separated): ").split()
        fuzzy_set[key] = float(value)
    return fuzzy_set

A = get_fuzzy_set("A")
B = get_fuzzy_set("B")

print("Union:", fuzzy_union(A, B))
print("Intersection:", fuzzy_intersection(A, B))
print("Complement of A:", fuzzy_complement(A))
print("A is subset of B:", is_subset(A, B))
print("De Morgan’s Law holds:", de_morgan_check(A, B))
