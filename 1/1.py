a = set([1,2,3])
b = set([1,2,3,4,5])

print(len(a), "U", len(b))
print("=", len(a.union(b)))

print(len(b), "-", len(a))
print("=", len(a.intersection(b)))

print(len(a), "+", len(b))
print(len(a) + len(b))
print("===")
print(len(a.union(b)) + len(a.intersection(b)))
