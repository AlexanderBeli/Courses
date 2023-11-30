# время видео 12:25
# задача найти все уникальные элементы в списке
l = [1, 2, 3, 1, 5, '123123', '3', '3']
l_unique = []
for i in l:
	if i not in l_unique:
		l_unique.append(i)
print(l_unique)

print(list(set(l)))

print(set(l))