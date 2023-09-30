# Уровень 1
#Даны три целых числа
#определить сколько совпадает

x1 = int(input('Число 1: '))
x2 = int(input('Число 2: '))
x3 = int(input('Число 3: '))

if x1 == x2 and x2 == x3:
	print(3)
elif x3 == x1 or (x2 == x1 or x3 == x2):
	print(2)
else:
	print(0)

#Уровень 2
#Шахматная ладья, данные
#YES or NO

lx1 = int(input())
ly1 = int(input())
lx2 = int(input())
ly2 = int(input())

if abs(lx1-lx2) == 0 or abs(ly1-ly2) == 0:
	print('YES')
else:
	print('NO')