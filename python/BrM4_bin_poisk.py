from random import randint

a = [randint(1, 50) for i in range(15)]
a.sort()
print(a)

value = int(input('Введите искоимую цифру: '))
pl = len(a) // 2

def search_value(value, a, pl):
	mid = len(a) // 2
	print(mid)

	if a[mid] == value:
		if pl < 0:
			pl = 5

		if pl > 14:
			pl = 14

		print(value, "находится под индексом ", pl)
		
	elif value > a[mid]: 
		pl += mid // 2 + 1
		search_value(value, a[mid:], pl)

	elif value < a[mid]:
		pl = pl - mid // 2 - 1
		search_value(value, a[:mid], pl)

	else:
		print('Такого числа в списке нет')


search_value(value, a, pl)	