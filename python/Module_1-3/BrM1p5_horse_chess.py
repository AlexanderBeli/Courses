#даны координаты двух коней на шахматной доске
#определить, бьют ли кони друг друга
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if (abs(x1 - x2) == 2) and (abs(y1 - y2) == 1):
	print('beaten')
elif (abs(x1 - x2) == 1) and (abs(y1 - y2) == 2):
	print('beaten')
else:
	print('no!!!')