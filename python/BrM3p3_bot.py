command = None
shopping_list = {}
while True:
	command = input('Введите команду ')
	if command == 'добавить':
		position = input('Введите название и количество через пробел')
		name, number = position.split()
		number = float(number)
		if name in shopping_list:
			shopping_list[name] += number
		else:
			shopping_list[name] = number
	elif command == 'удалить':
		position = input('Введите название позиции, которую хотите удалить')
		shopping_list.pop(position, None)
	elif command == 'показать':
		keys = sorted(shopping_list.keys())
		for key in keys:
			print(key, shopping_list[key])
	elif command == 'выход':
		break
	else:
		print('Я вас не понял, введите одну из комманд: [добавить, удалить, показать, выход]')