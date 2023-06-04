t = (1, 2, 3)
#t[0] = 3 				ошибка

table = [
("Alice", 25, 30),
("Bob", 27, 80),
("Charlie", 30, 90)
]
#print(table)
person = ("Alice", 25, 50)
name, age, weight = person
print(name)
name, age, weight = name, weight, age
print(age)

l = [1, 2, 3]
print(l)
ll = tuple(l)
print(ll)
#ll[0] = 5 				ошибка
lll = list(t)
print(lll)

table[0] = 1
#table[1][1] = 45 		ошибка
print(table[1][1])