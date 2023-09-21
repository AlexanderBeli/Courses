#Цель - добавить список слов в словарь
import json
import pickle
import re

if __name__ == "__main__":

	eng_dict = {}
	file_source = 'source.txt'
	dict_source = 'eng_dict.pickle'
	type_source = 'abbreviation.txt'

with open(dict_source, 'rb') as f:
	dict_data = pickle.load(f)

class Check:
	def __init__(self, stroke):
		self.stroke = stroke

		if not isinstance(stroke, str):
			print("It's not a string. Please check what you type.")
			return None

	#проверка на корректность ввода слова/ слов
	def check_w(self, word):
		self.word = word
		#чтобы все буквы после первой были lowcase, чтобы не было спец.символов, цифр; была только латиница
		#две ситуации
		#передано ключевое слово
		#передан список
		if len(word.split()) == 1:
			if re.search(r'[^a-zA-Z]',word ):
			     print("'It's not the word. Please try again")
			else:
			     print('correct word')

		else:
			word = word.replace(' ','').replace('↑','').replace(',','')

			if re.search(r'[^a-zA-Z]',word ):
			     print('The list of words consists of special characters or numbers. Please check the list and try again.')
			else:
			     print('The correct list of words')

#			if word.isalpha():
#				print('The correct list of words')
#			else:				
#				print('The list of words consists of special characters. Please check the list and try again.')

	#проверяем слово на наличие в словаре
	def check_key_word(self, name, dict_data):
		self.name = name

		if self.name in dict_data.keys():
			print(f'{name} is in the dictionary')
		else:
			print(f'{name} is a new word')

	#проверяем тип слова на наличие в списке 
	def check_type(self, w_type):
		self.w_type = w_type
		with open(type_source, 'r', encoding='utf-8') as f:
			type_data = f.read()

		if w_type in type_data:
			print('Yes')
		else:
			print('No')

	#можно перепроверить введенные слова на их наличие
	#а можно преобразовать словарь в формат множества, тогда при добавлении будут просто добавляться новые слова, исключаем вероятность повторения
	#Object of type set is not JSON serializable
	#Стал использовать pickle 21.09.2023


name = input('Please type here the word, which you want to add to the dict: ')

word = Check(name)
word.check_w(name)
word.check_key_word(name, dict_data)
#print(name.isalpha())
word.check_w(name)
print(word)
'''if name.isalpha():
	print('correct word')
#	return word
else:				
	print('not word')
'''#	return None
'''
#нужно перепроверить веденное слово - есть ли оно в словаре
# ответ да/нет
# нет - продолжаем процесс
# да - выдаем информацию, что оно есть в словаре
	#спрашиваем, какую категорию хочет добавить
	#проверяем категорию по abbreviation.txt и по наличию категории в словаре
		#Если категории нет в списке, выдать оповещение - "категории нет в списке, свяжитесь с разработчиком" и оборвать процесс
		#Если категория есть в списке, выдать оповещение "категория есть в списке" и "добавьте слова"/загружайте слова
		#Если категория есть в списке и есть в словаре - выдать информацию "Категория уже есть в словаре. Возможно слова, которые вы хотите добавить, уже находятся в словаре"
			#Сделать проверку, есть ли слова в словаре в данной категории
				#Если нет, то добавить

#нужно спросить откуда поступает база - вручную ввводим или из файла 

way = input('Do you want to download the data from the file? Use yes/no: ')
if way == 'yes':
#спросить к каой категории относится список слов, испльзовать утвержденный список
#проверить его ответ по abbreviation.txt. Если категории нет в списке, выдать оповещение - "категории нет в списке, свяжитесь с разработчиком" и оборвать процесс
	
	...
elif way == 'no':
#предлагаем ввести слова через запятую с пробелом
#нужно перепроверить введенные слова на отсутствие русских букв, спец символов
#сохранить список в source.txt на случай, чтобы потом перепроверить данные. Возможно, добавляя в название файла ключевое слово, для которого вводим данные
	...
else:
	print("You didn't answer correctly. Please, restart the program")
	return None



with open(file_source, 'r', encoding='utf-8') as f:
	n = f.read()

print(type(n))

n = n.replace('↑','').replace(',','')
n = n.split()

#nouns = set(n)	#для создания множества

#eng_dict = {name:n}

import json

with open('eng_dict.json', 'r', encoding='utf-8') as f:
	eng_dict = json.load(f)

if name not in eng_dict.keys():
	eng_dict[name] = n
	print("added ", name)
#	print(eng_dict)
else:
	print(name, " already exists")


with open('eng_dict.json', 'w', encoding='utf-8') as f:
	json.dump(eng_dict, f)

#print(eng_dict)
#import pickle

#my_pickled_object = pickle.dumps(nouns)
#print(f"This is my pickled object:\n{my_pickled_object}\n")

#my_unpickled_object = pickle.loads(my_pickled_object)
#print(f"This is my unpickled object:\n{my_unpickled_object}\n")

#with open('important','wb') as file:
#	pickle.dump(nouns, file)

#with open('important','rb') as file:
#	data = pickle.load(file)

#print(data)
'''