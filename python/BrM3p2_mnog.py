s = {1, 2, 3}
print(s)
a = type(s)
print(a)
s.add(1)
s.add(4)
print(s)
s.remove(1)
print(s)
s2 = {2,3}
s2.intersection(s)
print(s2)
k = s.union(s2)
print(k)
b = s.difference(s2)
print(b)


