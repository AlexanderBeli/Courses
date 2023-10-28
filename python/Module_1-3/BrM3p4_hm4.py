#registration_data = {}

import json


def register(log, passw):
	with open('login_pswd.json', 'r') as f:
		registration_data = json.load(f)	

	if log not in registration_data.keys():
		registration_data[log] = passwd
		with open('login_pswd.json', 'w', encoding='utf-8') as f:
			json.dump(registration_data, f)

	else:
		print('Login already exists')


def login_function(log, passw):
	with open('login_pswd.json', 'r') as f:
		registration_data = json.load(f)

	if log in registration_data.keys():
		if passw == registration_data[log]:
			print('Success!')
#			break

		else:
			print('Your password is not correct. Try again ')

	else:
		print('Your login does not exist. Sign in! ')




while True:
	q1 = input('Sign in? ')
	if q1 == 'no':
		q2 = input('Sign up? ')
		if q2 == 'no':
			break

		login = input('Write your login: ')
		passwd = input('Write your passwd: ')
		login_function(login, passwd)
		break

	login = input('Write your login: ')
	passwd = input('Write your passwd: ')

	register(login, passwd)