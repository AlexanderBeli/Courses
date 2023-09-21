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

with open('abbreviation.txt', 'r', encoding='utf-8') as f:
	type_data = f.read()

print(type_data)
#list_type = type_data.split()
#print(list_type)
check_type_w = 'adv'
if check_type_w in type_data:
	print('Yes')
else:
	print('No')