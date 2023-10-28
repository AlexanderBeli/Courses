# Уровень 1
#Даны три целых числа
#определить сколько совпадает

x1 = int(input('Число 1: '))
x2 = int(input('Число 2: '))
x3 = int(input('Число 3: '))

if x1 == x2 or (x2 == x3 or x1 == x3): 
	if x1 == x3:
		print(3)
	else:
		print(2)
else:
	print(0)

# Уровень 2
#Шахматная ладья
# YES NO - из одной клетки в другую

lx1 = int(input())
ly1 = int(input())
lx2 = int(input())
ly2 = int(input())

if abs(x1-x2) ==