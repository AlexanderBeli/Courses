#Цель - добавить список слов в словарь

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

posetive_answers = ('yes', 'y')
negative_answers = ('no', 'n')
middle_message = "We're checking that "
final_message = "There is no another option here. You may restart the program or connect to the developers. Goodbye! "
result_message = "We've added it to the dictionary. "
choice_message = "Please choose and write one of the next categories: word, meaning, collocations, categories"

class Check:
	def __init__(self, stroke):
		self.stroke = stroke

		if not isinstance(stroke, str):
			print("It's not a string. Please check what you typed.")
			return None

	#проверка на корректность ввода слова/ слов
	def check_w(self, word):
		self.word = word
		#чтобы все буквы после первой были lowcase, чтобы не было спец.символов, цифр; была только латиница
		#две ситуации
		#передано ключевое слово
		#передан список
		if len(word.split(',')) == 1:
			if re.search(r'[^a-zA-Z]',word ):
			     print("'It's not the word. Please try again")
			else:
			     return 1

		else:
			word = word.replace(' ','').replace('↑','').replace(',','')

			if re.search(r'[^a-zA-Z]',word ):
			     print('The list of words or text consists of special characters or numbers. Please check the list or text and try again.')
			else:
			     return 1

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
			return 1
		else:
			print("The category ", w_type, "doesn't exist. Please try again or check the categories. ")

	def check_collocations_in_category(self, name, category, data):
		self.name = name
		self.category = category
		self.data = data		

		if category in dict_data[name]['collocations'].keys():
			print(middle_message)
			inter_data = dict_data[name]['collocations'][category]
			inter_data_result = inter_data.union(data)
			dict_data[name]['collocations'][category] = inter_data_result
			print(result_message)
			print(dict_data[name]['collocations'][category])
		else:
			dict_data[name]['collocations'][category] = data
			print(result_message)
			print(dict_data[name]['collocations'][category])
	#можно перепроверить введенные слова на их наличие
	#а можно преобразовать словарь в формат множества, тогда при добавлении будут просто добавляться новые слова, исключаем вероятность повторения
	#Object of type set is not JSON serializable
	#Стал использовать pickle 21.09.2023

class Query():
	def __init__(self, stroke):
		self.stroke = stroke

	def key_word_step(self, ans):
		self.ans = ans

		name = input('Please type here the WORD that you want to add to the dictionary: ')
		print(middle_message)

		#осуществим проверку
		if name not in dict_data.keys():
			check_in = Check(name)
			if check_in.check_w(name) == 1:
				dict_data[name] = 'a new word in the dictionary'
				print(result_message)
		
		else:
			print(name, " already exists. Try again. ")

	def add_meaning_step(self, ans):
		self.ans = ans

		name = input('Please type here the WORD that you want to add the meaning: ')		
		print(middle_message)

		#осуществим проверку
		if name in dict_data.keys():
			category = input(f"Please type the CATEGORY of the {name} here: ")
			check_in = Check(category)
			if check_in.check_type(category) == 1:
				meaning = input(f"Please type the MEANING of the {name} here: ")
				if check_in.check_w(meaning) == 1:
					dict_data[name]['meaning'][category] = meaning
					print(result_message)

		else:
			print(name, "is not in the dictionary. Please try again or recheck the word. ")

	def add_collocations_step(self, ans):
		self.ans = ans

		name = input('Please type here the WORD that you want to add the collocations: ')		
		print(middle_message)

		#осуществим проверку
		if name in dict_data.keys():
			category = input(f"Please type the CATEGORY of the collocations here: ")
			check_in = Check(category)
			if check_in.check_type(category) == 1:
				collocations_request = input("Do you want to download the collocations from the file? Use yes/no: ")

				if collocations_request in posetive_answers:
					with open(file_source, 'r', encoding='utf-8') as collocations_source:
						collocations = collocations_source.read()

					if check_in.check_w(collocations) == 1:
						#нужно преобразовать в set через запятые и добавить в словарь
						collocations = collocations.replace('↑','').replace(', ',',')
						set_collocations = set(collocations.split(','))

						print(name, category, set_collocations)
						#if check_in.check_collocations_in_category(name, category, set_collocations) == 1:
						#	dict_data[name]['collocations'][category] = set_collocations
						#	print(result_message)							

				elif collocations_request in negative_answers:

					collocations = input(f"Please type the COLLOCATIONS of the {name} here using ',' and blank space: ")
			
					if check_in.check_w(collocations) == 1:
						#нужно преобразовать в set через запятые и добавить в словарь
						collocations = collocations.replace('↑','').replace(', ',',')
						set_collocations = set(collocations.split(','))

						print(name, category, set_collocations)
						check_in.check_collocations_in_category(name, category, set_collocations)
				else:
					print("Your answer to the question is wrong. Please try again. ")
		else:
			print(name, " is not in the dictionary. Please try again or recheck the word. ")

#след усовуршенствованная логика процесса Update 3.0

while True:
	step = input("What do you want to do? Type the one of the next commands: show, add, change, delete or exit. ")
	process = Query(step)

	if step == 'show':
		step2 = input(choice_message)
			if step2 == 'word':
				print(middle_message)

			elif step2 == 'meaning':
				print(middle_message)

			elif step2 == 'collocations':
				print(middle_message)

			elif step2 == 'categories':
				print(middle_message)

			else:
 				print(final_message)

	elif step == 'add':
		step2 = input(choice_message)
			if step2 == 'word':
				print(middle_message)

			elif step2 == 'meaning':
				print(middle_message)

			elif step2 == 'collocations':
				print(middle_message)
				process.add_collocations_step(step)
				
			elif step2 == 'categories':
				print(middle_message)

			else:
 				print(final_message)

	elif step == 'change':
		step2 = input(choice_message)
			if step2 == 'word':
				print(middle_message)

			elif step2 == 'meaning':
				print(middle_message)

			elif step2 == 'collocations':
				print(middle_message)

			elif step2 == 'categories':
				print(middle_message)

			else:
 				print(final_message)

	elif step == 'delete':
		step2 = input(choice_message)
			if step2 == 'word':
				print(middle_message)

			elif step2 == 'meaning':
				print(middle_message)

			elif step2 == 'collocations':
				print(middle_message)

			elif step2 == 'categories':
				print(middle_message)

			else:
 				print(final_message)

	elif step == 'exit':
		break

	else:
		print(final_message)
		break
'''
#Логика процесса Update 2.0
step = input('Do you want to add the new word to the English dictionary? Use yes/no: ')
process_one = Query(step)

if step in posetive_answers:	
	process_one.key_word_step(step)

elif step in negative_answers:
	step2 = input('Do you want to add some extra information or collocations to the existant word in the English dictionary? Use yes/no: ')

	if step2 in posetive_answers:
		step3 = input('Do you want to add the meaning of the existant word in the English dictionary? Use yes/no: ')

		if step3 in posetive_answers:
			process_one.add_meaning_step(step3)

		else:
			step4 = input('Do you want to add collocations to the existant word in the English dictionary? Use yes/no: ')

			if step4 in posetive_answers:
				process_one.add_collocations_step(step4)

			else:
				print(final_message)
	else:
		print(final_message)
else:
	print(final_message)
'''