from add_word import*

with open(dict_source, 'rb') as f:
	dict_data = pickle.load(f)

for i in dict_data:
	for j in dict_data[i]:
		print(i, j, dict_data[i][j]['meaning'])
'''
#изменение abbreviation на adj
for i in dict_data.keys():
	dict_data[i]['meaning'] = {'adj':'description'} 

print(dict_data['key']['meaning'])

with open(dict_source, 'wb') as change_abr:
	pickle.dump(dict_data, change_abr)
'''
'''
 #изменение порядка отражения, перемещения типа слова на второе место
for i in (dict_data):
	new = {'adj':dict_data[i]}
	dict_data[i] = new

with open(dict_source, 'wb') as change_step:
	pickle.dump(dict_data, change_step)
'''
'''
#подкорректировал 'meaning'
for i in dict_data.keys():
	dict_data[i]['adj']['meaning'] = 'description'

with open(dict_source, 'wb') as change_meaning:
	pickle.dump(dict_data, change_meaning)
'''
