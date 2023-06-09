capital_by_country = {
	'Россия': 'Москва',
	'США': 'Вашингтон',
	'Китай': 'Пекин',
}
print(capital_by_country['Россия'])
capital_by_country['Казахстан'] = 'Астана'
print(capital_by_country)
capital_by_country['Казахстан'] = 'Нур-Султан'
print(capital_by_country)
print('Германия' in capital_by_country)				#False
print('Казахстан' in capital_by_country)			#True
print(capital_by_country.get('Германия','Нет информации'))
print(capital_by_country.get('Казахстан','Нет информации'))
print(capital_by_country)
value = capital_by_country.pop('Казахстан','Нет информации')
print(value)
print(capital_by_country)							#Теперь здесь нет Казахстана