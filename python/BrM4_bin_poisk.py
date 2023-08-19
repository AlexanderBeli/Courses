from random import randint

a = [randint(1, 50) for i in range(15)]
a.sort()
print(a)

value = int(input('Введите искоимую цифру: '))

def search_value(value, a):
	mid = len(a) // 2
	print(mid)
	
	if a[mid] != value:
		search_value(value, a[:mid])
		search_value(value, a[mid:])

		print(mid)
	else:
		print(mid)






#search_value(value, a)	