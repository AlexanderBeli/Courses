name ='key'
name2 ='important'
name3 ='significant'
file = f'results_{name}_{name2}_{name3}.txt'

def sor_lis(x):
	return sorted(list(x))

import json

with open('eng_dict.json','r',encoding='utf-8') as f:
	eng_dict = json.load(f)

for word, voc in eng_dict.items():
	print(word) 

#подготовка к записи - отображение в столбик
for n, voc in eng_dict.items():
	for i in range(0,len(eng_dict[f'{n}'])):
		eng_dict[n][i] = eng_dict[n][i] + '\n'


set_name = set(eng_dict[f'{name}'])
set_name2 = set(eng_dict[f'{name2}'])
set_name3 = set(eng_dict[f'{name3}'])


#слова, свойственные всем трем
all_names = set_name.intersection(set_name2, set_name3)
list_all_names = sorted(list(all_names))


#запись результата в текстовый файл
list_all_names = ''.join(list_all_names)
list_all_names_extra = 'The list of all words bellow: \n'

with open(file, 'w', encoding='utf-8') as f:
	f.write(list_all_names_extra + list_all_names)

#слова, свойственные только двум 
#вначале надо вычесть предыдущие слова. Добавим их в значения, которые и дальше будем использовать
set_name = set_name.difference(all_names)
set_name2 = set_name2.difference(all_names)
set_name3 = set_name3.difference(all_names)

'''
print(sor_lis(set_name), '\n')
print(sor_lis(set_name2), '\n')
print(sor_lis(set_name3), '\n')
'''
name_name2 = set_name.intersection(set_name2)
name_name3 = set_name.intersection(set_name3)
name3_name2 = set_name3.intersection(set_name2)


#подготовка и запись результата в текстовый файл
list_name_name2 = sor_lis(name_name2)
list_name_name3 = sor_lis(name_name3)
list_name3_name2 = sor_lis(name3_name2)

list_name_name2 = ''.join(list_name_name2)
list_name_name3 = ''.join(list_name_name3)
list_name3_name2 = ''.join(list_name3_name2)

'''
print(list_name_name2, '\n')
print(list_name_name3, '\n')
print(list_name3_name2, '\n')
'''

list_extra = '\n \n The list of '

with open(file, 'a', encoding='utf-8') as f:
	f.write(list_extra + name + ' and ' + name2 + '\n' +list_name_name2)
	f.write(list_extra + name + ' and ' + name3 + '\n' +list_name_name3)
	f.write(list_extra + name3 + ' and ' + name2 + '\n' +list_name3_name2)


#слова, свойственные только одному
dif_name = set_name.difference(set_name2, set_name3)
dif_name2 = set_name2.difference(set_name, set_name3)
dif_name3 = set_name3.difference(set_name2, set_name)

#подготовка и запись результата в текстовый файл
list_dif_name = sorted(list(dif_name))
list_dif_name2 = sorted(list(dif_name2))
list_dif_name3 = sorted(list(dif_name3))

list_dif_name = ''.join(list_dif_name)
list_dif_name2 = ''.join(list_dif_name2)
list_dif_name3 = ''.join(list_dif_name3)

with open('results.txt', 'a', encoding='utf-8') as f:
	f.write(list_extra + name + '\n' +list_dif_name)
	f.write(list_extra + name2 + '\n' +list_dif_name2)
	f.write(list_extra + name3 + '\n' +list_dif_name3)