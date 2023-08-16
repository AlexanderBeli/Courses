#вклад в банке

x = float(input('Введите сумму вклада в банке '))
p = float(input('Введите ежегодный процент вклада '))
y = float(input('Введите сумму, которую вы хотите получить '))
t = 0

while x < y:
	x = abs(x * p / 100) + x 		#годовой доход, по условиям задачи нужно округлить
	t = t + 1

print(t+1)


#цикл for и while

n = int(input('Введите число повторений '))
z = 0

while n > 0 :
	print('for - частный случай цикла while ', n, ' раз')
	n = n - 1


#подсчитать сумму цифр целого числа

number = input('Введите произвольное число ')
s = 0
l = len(number)

for x in range (0,l):
	y = int(number[x])
#	print(x, y, end=', ')
	s += y
#	print(s)

print(s)