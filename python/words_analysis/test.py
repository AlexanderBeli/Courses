'''a = {}
b = {'alex', 'John', 'Ris'}
c = {'Anna', 'Janet', 'Juliette'}
a = {'family': {'names' : [{'mus_names': b}, {'fem_names': c}]}}

print(type(a))
print(a)

print(a['family']['names'][0]['mus_names'])'''

'''name = 'key'

word = name.split()

print(word)
print(type(word))
print(len(word))'''

'''a = ['key']
b = ''.join(a)
print(b)'''

import re

'''a = "testтест"

if re.search(r'[^a-zA-Zа-яА-Я]',a ):
     print("error")
else:
     print("ok")

a = "test4тест"

if re.search(r'[^a-zA-Zа-яА-Я]',a ):
    print("error")
else:
    print("ok")'''

'''with open('abbreviation.txt', 'r', encoding='utf-8') as f:
	type_data = f.read()

print(type_data)
#list_type = type_data.split()
#print(list_type)
check_type_w = 'adv'
if check_type_w in type_data:
	print('Yes')
else:
	print('No')'''

'''name = "mother, son, ball and bicicle, 123"
name = name.replace(', ',',')
test = set(name.split(','))
print(test)'''

middle_message = "We're checking that "
while True:
	step7 = input("What do you want to do? Type the one of the next commands: add, change, delete or exit. ")

	if step7 == 'add':
		print(middle_message)

	elif step7 == 'change':
		print(middle_message)

	elif step7 == 'delete':
		print(middle_message)

	elif step7 == 'exit':
		break

	else:
		break
