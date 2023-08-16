data_pizza = {'margarita':400, 'carbonara':500}


def add_pizza(name, price):
	if name not in data_pizza.keys():
		data_pizza[name] = price
	else:
		print('Pizza already exists')


def del_pizza(name):
	if name in data_pizza.keys():
		del data_pizza[name]
	else:
		print('Pizza not exists')


def order_pizza():
	order =[]
	cost = 0
	while True:
		q1 = input('Continue?')
		if q1 == 'no':
			break
		pizza_name = input()
		if pizza_name in data_pizza.keys():
			order.append(pizza_name)
			cost += data_pizza[pizza_name]
			print('Pizza added')
	return {'order': order, 'cost': cost}


while True: 
	break_point = input('Stop?')
	if break_point == 'yes':
		break

	chose_role = input('Chose role?')
	if chose_role == 'user':
		print(order_pizza())

	else:
		q2 = input('Add or delete ')
		if q2 == 'del':
			del_pizza(input('Pizza name?'))
		elif q2 == 'add':
			add_pizza(input('Pizza name?'), int(input('Price')))