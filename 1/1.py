a = set([1,2,3])
b = set([1,2,3,4,8,20])
print("a:", a)
print("b:", b)

print(len(a), "U", len(b))
uab = a.union(b)
print("=", len(uab))

print(len(b), "-", len(a))
iab = a.intersection(b)
print("=", len(iab))

print("\nSize of union plus size of intersection")
print(len(a), "+", len(b))
print("===")
print("sum of set sizes:")
print(len(uab), "+", len(iab))

print(len(a) + len(b))
print("===")
print(len(uab) + len(iab))

print("----------")

print("valuation function v: mean")
def v(a):
	return sum(a)/len(a)
	
print(v(a), "U", v(b))
print("=", v(uab))

print(v(b), "-", v(a))
iab = a.intersection(b)
print("=", v(iab))

print("\nSize of union plus size of intersection")
print(v(a), "+", v(b))
print("===")
print("sum of set means:")
print(v(uab), "+", v(iab))

print("----------")

print("valuation function v: double size")
def v(a):
	return len(a) * 2
	
print(v(a), "U", v(b))
print("=", v(uab))

print(v(b), "-", v(a))
iab = a.intersection(b)
print("=", v(iab))

print("\nSize of union plus size of intersection")
print(v(a), "+", v(b))
print("===")
print("sum of set means:")
print(v(uab), "+", v(iab))
