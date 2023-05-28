#Пользователь вводит 3 числа
#Найти Max
a = float(input('Введите первое число:'))
b = float(input('Введите второе число:'))
c = float(input('Введите третье число:'))
#max1 = (a>=b & a>=c)*a + (b>a & b>=c)*b + (c>a & c>b)*c
#print('Max:', max1)
#добавим условие: пользователи могут вводить дробные числа. 
#если ввели целые - покажем целые, если дробные, то дробные 
#при работе с отрицательными числами есть нюанс - доработать хотелось бы
if a>=b and a>=c:
	if a >= 0:
		if a > int(a):
			print('Max:', a)
		else:
			print('Max:', int(a))
	else:
		if a < int(a):
			print('Max:', a)
		else:
			print('Max:', int(a))
elif b>=a and b>=c:
	if b >= 0:
		if b > int(b):
			print('Max:', b)
		else:
			print('Max:', int(b))
	else:
		if b < int(b):
			print('Max:', b)
		else:
			print('Max:', int(b))
elif c>=a and c>=b:
	if c >= 0:
		if c > int(c):
			print('Max:', c)
		else:
			print('Max:', int(c))
	else:
		if c < int(c):
			print('Max:', c)
		else:
			print('Max:', int(c))
else:
	print('Thank you for your participation!')
#if x >= y:
#	if x >= z:
#		print(x)
#	else:
#		print(z)
#else:
#	if y >= z:
#		print(y)
#	else:
#		print(z)