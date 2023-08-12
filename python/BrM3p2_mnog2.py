#система регистрации и проверки входа по логину и паролю
data = {'testlog':'testpasswd'}
secret_info = '42'
while True:
	pass
	q1 = input('Вход или регистрация? ')
	if q1 == 'вход':
		log = input('Введите логин: ')
		psswd = input('Введите пароль: ')
		if log in data.keys():
			if data[log] == psswd:
				print('Успешный вход!')
				print(secret_info)
		else:
			print('Неверный логин')
	elif q1 == 'регистрация':
		log = input('Введите логин: ')
		psswd = input('Введите пароль: ')
		if log in data.keys():
			print('Логин занят')
		else:
			data[log] = psswd
			print('Регистрация успешно')