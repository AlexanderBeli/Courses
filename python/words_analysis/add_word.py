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

#if __name__ == "__main__":

eng_dict = {}
file_source = 'source.txt'
dict_source = 'eng_dict.pickle'
type_source = 'abbreviation.txt'

posetive_answers = ('yes', 'y')
negative_answers = ('no', 'n')
first_message = "What do you want to do? Type the one of the next commands: show, add, change, delete or exit. "
first_answer_show = ('show', 's', 'sh', 'sho', 'show')
first_answer_add = ('add', 'ad', 'a')
first_answer_change = ('change', 'chang', 'chan', 'ch', 'c')
first_answer_delete = ('delete', 'delet', 'dele', 'del', 'de', 'd')
first_answer_exit = ('exit', 'exi', 'ex', 'e')
middle_message = "We're checking that "
final_message = "There is no another option here. You may restart the program or connect to the developers. Goodbye! "
error_message = "There is no such relevant information in the dictionary. Please check what your wrote and try again. "
result_message = "We've added it to the dictionary. "
del_suc_message = "We've removed it"
ch_suc_message = "We've changed it"
choice_message = "Please choose and write one of the next categories: word, meaning, collocations, categories "
choice_answer_word = ('word', 'wor', 'wo', 'w')
choice_answer_meaning = ('meaning', 'meanin', 'meani', 'mean', 'mea', 'me','m')
choice_answer_collocations = ('collocations', 'collocation', 'collocatio','collocati', 'collocat', 'colloca', 'colloc', 'collo', 'coll', 'col', 'co', 'c')
choice_answer_category = ('category', 'categor', 'catego', 'categ', 'cate', 'cat', 'ca')
#при запросе ввода информации указать: Если вы хотите выйти из режима/завершить напишите 'exit'

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
			print("The category ", w_type, " doesn't exist. Please try again or check the categories. ")

	def check_collocations_in_category(self, name, category):
		self.name = name
		self.category = category		

		if category in dict_data[name]['collocations'].keys():
			return 1
		else:
			return 0
			
	#можно перепроверить введенные слова на их наличие
	#а можно преобразовать словарь в формат множества, тогда при добавлении будут просто добавляться новые слова, исключаем вероятность повторения
	#Object of type set is not JSON serializable
	#Стал использовать pickle 21.09.2023


class ShowVoc:
	def __init__(self, stroke):
		self.stroke = stroke

		if not isinstance(stroke, str):
			print("It's not a string. Please check what you typed.")
			return None

	def show_words(self, ans):
		self.ans = ans
		print(sorted(list(dict_data.keys())))

	def show_meaning(self, ans):
		self.ans = ans
		name = input("Write the WORD that meaning you want to read: ")

		if name in dict_data.keys():
			for i, k in dict_data[name]['meaning'].items():
				print(f"{name} \n {i}:\n {k}\n")
		else:
			print(error_message)

	def show_collocations(self, ans):
		self.ans = ans
		name = input("Write the WORD that collocations you want to read: ")

		if name in dict_data.keys():
			for i, k in dict_data[name]['collocations'].items():
				collocations_data = sorted(list(dict_data[name]['collocations'][i]))
				print(f"{name} \n {i}:\n {collocations_data}\n")
		else:
			print(error_message)

	def show_category(self, ans):
		self.ans = ans

		print(category_list_data)


class AddVoc:
	def __init__(self, stroke):
		self.stroke = stroke

		if not isinstance(stroke, str):
			print("It's not a string. Please check what you typed.")
			return None

	def add_key_word_step(self, ans):
		self.ans = ans

		name = input('Please type here the WORD that you want to add to the dictionary: ')
		print(middle_message)

		#осуществим проверку
		if name not in dict_data.keys():
			check_in = Check(name)
			if check_in.check_w(name) == 1:
				dict_data[name] = 'a new word in the dictionary'
				with open(dict_source, 'wb') as upload_new_word:
					pickle.dump(dict_data, upload_new_word)
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
					with open(dict_source, 'wb') as upload_new_meaning:
						pickle.dump(dict_data, upload_new_meaning)
					print(result_message)

		else:
			print(name, "is not in the dictionary. Please try again or recheck the word. ")

	def add_collocations_step(self, ans):
		self.ans = ans

		name = input('Please type here the WORD that you want to add the collocations: ')		
		print(middle_message)

		#осуществим проверку
		if name in dict_data.keys():
			category = input("Please type the CATEGORY of the collocations here: ")
			check_in = Check(category)
			if check_in.check_type(category) == 1:
				collocations_request = input("Do you want to download the collocations from the file? Use yes/no: ")
				set_collocations = 0

				if collocations_request in posetive_answers:
					with open(file_source, 'r', encoding='utf-8') as collocations_source:
						collocations = collocations_source.read()

					if check_in.check_w(collocations) == 1:
						#нужно преобразовать в set через запятые и добавить в словарь
						collocations = collocations.replace('↑','').replace(', ',',')
						set_collocations = set(collocations.split(','))						

				elif collocations_request in negative_answers:

					collocations = input(f"Please type the COLLOCATIONS of the {name} here using ',' and blank space: ")
			
					if check_in.check_w(collocations) == 1:
						#нужно преобразовать в set через запятые и добавить в словарь
						collocations = collocations.replace('↑','').replace(', ',',')
						set_collocations = set(collocations.split(','))
				else:
					print("Your answer to the question is wrong. Please try again. ")

				#проверяем наличие и добавляем
				if set_collocations != 0:
					if check_in.check_collocations_in_category(name, category) == 1:
						inter_data = dict_data[name]['collocations'][category]
						inter_data_result = inter_data.union(set_collocations)
						dict_data[name]['collocations'][category] = inter_data_result
						with open(dict_source, 'wb') as upload_new_collocations:
							pickle.dump(dict_data, upload_new_collocations)
						print(result_message)
					else:
						dict_data[name]['collocations'][category] = set_collocations
						with open(dict_source, 'wb') as upload_new_collocations:
							pickle.dump(dict_data, upload_new_collocations)
						print(result_message)
		else:
			print(name, " is not in the dictionary. Please try again or add the word first. ")

	def add_category_step(self, ans):
		self.ans = ans

		name = input('Please type here the CATEGORY ABBREVIATION that you want to add the list: ')		
		print(middle_message)

		#осуществим проверку
		if name not in category_list_data:
			check_in = Check(name)
			if check_in.check_w(name) == 1:
				with open(type_source, 'a', encoding='utf-8') as add_category_list:
					add_category_list.write(f"{name} \n")
				print("The category ", name, " has added. ")
		else:
			print("The category ", name, "already exists. ")


class ChangeVoc:
	def __init__(self, stroke):
		self.stroke = stroke

		if not isinstance(stroke, str):
			print("It's not a string. Please check what you typed.")
			return None

	def change_word(self, ans):
		self.ans = ans

		change_info = input("Write the WORD you want to change: ")

		if change_info in dict_data.keys():
			change_string = input("Write the correct WORD: ")
			check_in.Check(change_string)
			if check_in.check_w(change_string) == 1:
				change_data = {change_string:dict_data[change_info]}
				dict_data.pop(change_info)
				dict_data[change_data]
				with open(dict_source, 'wb') as change_word:
					pickle.dump(dict_data, change_word)
				print(ch_suc_message)
		else:
			print(error_message)

	def change_meaning(self, ans):
		self.ans = ans

		change_info = input("Write the WORD that meaning you want to change: ")

		if change_info in dict_data.keys():
			extra_info = input("Write the CATEGORY the meaning you want to change: ")
			if extra_info in dict_data[change_info]['meaning'].keys():
				print(dict_data[change_info]['meaning'][extra_info])
				new_meaning = input("Write the new MEANING: ")
				dict_data[change_info]['meaning'][extra_info] = new_meaning
				with open(dict_source, 'wb') as change_meaning:
					pickle.dump(dict_data, change_meaning)
				print(ch_suc_message)
			else:
				print(error_message)
		else:
			print(error_message)

	def change_collocations(self, ans):
		self.ans = ans

		change_info = input("Write the WORD that collocations you want to change: ")

		if change_info in dict_data.keys():
			extra_info = input("Write the CATEGORY the collocations you want to change: ")
			if extra_info in dict_data[change_info]['collocations'].keys():
				changing_set = dict_data[change_info]['collocations'][extra_info]
				changing_list = sorted(list(dict_data[change_info]['collocations'][extra_info]))
				print(changing_list)	
				while True:
					new_change_request = input("Write the WORD from the list which you want to change. If you want to replace the whole list, first delete and than add it. For going out write 'exit': ")
					if new_change_request in changing_set:
						changing_word = input("Write the correct word: ")
						check_in = Check(changing_word)
						if check_in.check_w(changing_word) == 1:
							changing_set.remove(new_change_request)
							changing_set.add(changing_word)
							dict_data[change_info]['collocations'][extra_info] = changing_set
							with open(dict_source, 'wb') as change_collocations:
								pickle.dump(dict_data, change_collocations)
							print(ch_suc_message)
					else:
						break
			else:
				print(error_message)
		else:
			print(error_message)

	def change_category(self, ans):
		self.ans = ans

		change_info = input("Write the CATEGORY you want to change: ")
		list_category = category_list_data.split(f'\n')
		if change_info in list_category:
			fixed_category = input("Write the CORRECT version of CATEGORY you want to add: ")
			new_category_list_data = category_list_data.replace(f'{change_info}\n', f'{fixed_category}\n')
			print(new_category_list_data)

			with open(type_source, 'w', encoding='utf-8') as fixed_category_list:
				fixed_category_list.write(new_category_list_data)
			print(ch_suc_message)
		else:
			print(error_message)


class DeleteVoc:
	def __init__(self, stroke):
		self.stroke = stroke

		if not isinstance(stroke, str):
			print("It's not a string. Please check what you typed.")
			return None

	def del_word(self, ans):
		self.ans = ans

		del_info = input("Write the WORD that you want to delete from the dictionary: ")

		if del_info in dict_data.keys():
			dict_data.pop(del_info)
			with open(dict_source, 'wb') as del_word:
				pickle.dump(dict_data, del_word)
			print(del_suc_message)
		else:
			print(error_message)

	def del_meaning(self, ans):
		self.ans = ans

		del_info = input("Write the WORD that meaning you want to delete from the dictionary: ")

		if del_info in dict_data.keys():
			extra_info = input("Write the CATEGORY that with the meaning you want to delete from the dictionary: ")
			if extra_info in dict_data[del_info]['meaning'].keys():
				dict_data[del_info]['meaning'].pop(extra_info)
				with open(dict_source, 'wb') as del_word:
					pickle.dump(dict_data, del_word)
				print(del_suc_message)
			else:
				print("The category is not on the list. ")
		else:
			print(error_message)

	def del_collocations(self, ans):
		self.ans = ans

		del_info = input("Write the WORD that collocations you want to delete from the dictionary: ")

		if del_info in dict_data.keys():
			extra_info = input("Write the CATEGORY the collocations you want to delete from the dictionary: ")
			if extra_info in dict_data[del_info]['collocations'].keys():
				del_set = dict_data[del_info]['collocations'][extra_info]
				del_list = sorted(list(dict_data[del_info]['collocations'][extra_info]))
				print(del_list)
				while True:
					new_del_request = input("Write the WORD from the list which you want to delete. If you want to delete the whole list write 'list'. For going out write 'exit': ")
					if new_del_request in del_set:
						del_set.remove(new_del_request)
						dict_data[del_info]['collocations'][extra_info] = del_set
						with open(dict_source, 'wb') as del_cols:
							pickle.dump(dict_data, del_cols)
						print(del_suc_message)

					elif new_del_request == 'list':
						dict_data[del_info]['collocations'].pop(extra_info)
						with open(dict_source, 'wb') as del_cols:
							pickle.dump(dict_data, del_cols)
						print(del_suc_message)
						break
					else:
						break
			else:
				print("The category is not on the list. ")
		else:
			print(error_message)

	def del_category(self, ans):
		self.ans = ans

		del_info = input("Write the CATEGORY that you want to delete from the list: ")
		list_category = category_list_data.split(f'\n')
		if del_info in list_category:
			new_category_list_data = category_list_data.replace(f'{del_info}\n', '')
			print(new_category_list_data)

			with open(type_source, 'w', encoding='utf-8') as new_category_list:
				new_category_list.write(new_category_list_data)
			print(del_suc_message)
		else:
			print(error_message)

#усовершенствованная логика процесса Update 3.3
if __name__ == "__main__":

	while True:
		with open(dict_source, 'rb') as f:
			dict_data = pickle.load(f)

		with open(type_source, 'r', encoding='utf-8') as category_list:
			category_list_data = category_list.read()

		step = input(first_message)

		if step in first_answer_show:
			step2 = input(choice_message)
			process = ShowVoc(step)

			if step2 in choice_answer_word:
				print(middle_message)
				process.show_words(step2)

			elif step2 in choice_answer_meaning:
				print(middle_message)
				process.show_meaning(step2)

			elif step2 in choice_answer_collocations:
				print(middle_message)
				process.show_collocations(step2)

			elif step2 in choice_answer_category:
				print(middle_message)
				process.show_category(step2)

			else:
	 			print(final_message)

		elif step in first_answer_add:
			step2 = input(choice_message)
			process = AddVoc(step)

			if step2 in choice_answer_word:
				print(middle_message)
				process.add_key_word_step(step2)

			elif step2 in choice_answer_meaning:
				print(middle_message)
				process.add_meaning_step(step2)

			elif step2 in choice_answer_collocations:
				print(middle_message)
				process.add_collocations_step(step2)

			elif step2 in choice_answer_category:
				print(middle_message)
				process.add_category_step(step2)

			else:
	 			print(final_message)

		elif step in first_answer_change:
			step2 = input(choice_message)
			process = ChangeVoc(step)

			if step2 in choice_answer_word:
				print(middle_message)
				process.change_word(step2)

			elif step2 in choice_answer_meaning:
				print(middle_message)
				process.change_meaning(step2)

			elif step2 in choice_answer_collocations:
				print(middle_message)
				process.change_collocations(step2)

			elif step2 in choice_answer_category:
				print(middle_message)
				process.change_category(step2)

			else:
	 			print(final_message)

		elif step in first_answer_delete:
			step2 = input(choice_message)
			process = DeleteVoc(step)

			if step2 in choice_answer_word:
				print(middle_message)
				process.del_word(step2)

			elif step2 in choice_answer_meaning:
				print(middle_message)
				process.del_meaning(step2)

			elif step2 in choice_answer_collocations:
				print(middle_message)
				process.del_collocations(step2)

			elif step2 in choice_answer_category:
				print(middle_message)
				process.del_category(step2)

			else:
	 			print(final_message)

		elif step in first_answer_exit:
			break

		else:
			print(final_message)
			break