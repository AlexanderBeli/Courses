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