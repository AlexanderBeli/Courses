from add_word import *
import os


if __name__ == "__main__":
	while True:
		with open(dict_source, 'rb') as f:
			dict_data = pickle.load(f)

		main_request = input("Do you want to compare some word's collocations? Use yes/no: ")
		if main_request in posetive_answers:
			#show_vocabulary = sorted(list(dict_data))
			print("You can see the full list of available words and categories below: ")

			for names in sorted(list(dict_data)):
				print(names, ' ', list(dict_data[names]['collocations']))

			number_of_words = int(input("Write the the NUMBER of comparing words: "))
			word = ''
			comparing_dict = {}
			result_dict = {}
			directory = 'results'
			result_file_name = 'results.txt'

			if number_of_words > 1:
				comparing_category = input("Write the comparing CATEGORY: ")
				check_in = Check(comparing_category)
				if check_in.check_type(comparing_category) == 1:

					for i in range(0, number_of_words):
						k = i+1
						word = input(f"Write the word number {k}: ")
						if check_in.check_w(word) == 1:
							if word in dict_data.keys():
								if word not in comparing_dict.keys():
									if len(comparing_dict) != 0:
										comparing_dict_of_one_word = {}
										comparing_dict_of_one_word[word] = {}
										comparing_dict_of_one_word[word][comparing_category] = dict_data[word]['collocations'][comparing_category]
										result_file_name = word + '_' + result_file_name

										for w in tuple(comparing_dict):
											new_comp_list = comparing_dict[w][comparing_category].intersection(comparing_dict_of_one_word[word][comparing_category])
											new_comp_list_name = word + '_' + w
											comparing_dict[new_comp_list_name] = {}
											comparing_dict[new_comp_list_name][comparing_category] = new_comp_list

											dif_old_comp_list = comparing_dict[w][comparing_category].difference(new_comp_list)
											comparing_dict[w][comparing_category] = dif_old_comp_list

											dif_word_list = comparing_dict_of_one_word[word][comparing_category].difference(new_comp_list)
											comparing_dict_of_one_word[word][comparing_category] = dif_word_list

										comparing_dict[word] = {}
										comparing_dict[word][comparing_category] = comparing_dict_of_one_word[word][comparing_category]

									else:
										#Если это первое слово
										comparing_dict[word] = {}
										comparing_dict[word][comparing_category] = dict_data[word]['collocations'][comparing_category]
										result_file_name = word + '_' + result_file_name
										#print(comparing_dict[word][comparing_category])

								else:
									print("You've already typed that word.")

							else:
								print(error_message)
								break
					#сформировали имя файла
					print(result_file_name)
					#сформировали словарь по ключевым словам с БД

					#запись результата в файл
					if not os.path.exists(directory):
						os.makedirs(directory)
					file_path = os.path.join(directory, result_file_name)

					with open(file_path, 'w', encoding='utf-8') as result_file:
						for x, y in comparing_dict.items():
							key_name = '\n' + '\t' + x + '\n'
							result_file.write(key_name)
							for o, p in comparing_dict[x].items():
								key_category = '\t' + "category: " + o + '\n' + '\n'
								result_file.write(key_category)


								key_collocations = sorted(list(p))
								for coll in range(0, len(p)):
									key_collocations[coll] = key_collocations[coll] + '\n' 
								key_collocations = ''.join(key_collocations)
								result_file.write(key_collocations)

					print("We've saved the result to the text file. Please check it. ")

			else:
				print("It's not a number. Restart the program and try again. ")
				break
		else:
			break
