correct_password = str(5556)
password = input('Введите пароль: ')
while password != correct_password:
	print('Неверный пароль')
	password = input('Введите пароль: ') 
