command = None
shopping_list = {}


def add_position(shopping_list):
	position = input('Введите название и количество через пробел ')
	name, number = position.split()
	number = float(number)

	if name in shopping_list:
		shopping_list[name] += number

	else:
		shopping_list[name] = number
	
	return shopping_list


def remove_position(shopping_list):
	position = input('Введите название позиции, которую хотите удалить ')
	shopping_list.pop(position, None)
	return shopping_list


def show_shopping_list(shopping_list):
	keys = sorted(shopping_list.keys())
	for key in keys:
		print(key, shopping_list[key])


def mistake():
	print('Я вас не понял, введите одну из команд: [добавить, удалить, показать, выход]')


def process(command, shopping_list):
	if command == 'добавить':
		shopping_list = add_position(shopping_list)

	elif command == 'удалить':
		shopping_list = remove_position(shopping_list)

	elif command == 'показать':
		 show_shopping_list(shopping_list)

	else:
		mistake()
	
	return

while  True:
	command = input('Введите комманду ')
	
	if command == 'выход':
		break
	
	process(command, shopping_list)

