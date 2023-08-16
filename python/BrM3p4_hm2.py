#произвольный список

l = [1, 4, 1, 6, "hello", "a", 5, "hello"]
print(set(l))

#матрица, найти max

k = [
[9, 70, 20, 67, 33],
[60, 20, 94, 14, 77],
[27, 58, 45, 0, 13],
[39, 47, 25, 97, 69],
[83, 13, 100, 1, 85]]

max_number = 0
rest = []

for i, val in enumerate(k):
	for x, y in enumerate(val):
		if val[x] > val[x-1]:
			rest.append(val[x])

max_number = max(rest)
print('max_number ', max_number)

#словарь, поменять ключи и значения
d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
c = {}

for x, y in d.items():
	c[y] = x

# нашел в интернете такое решение, не до конца понимаю синтаксис, объясните, пожалуйста
# c = {v:k for k,v in d.items()}

print(c)