from add_word import *
import os


if __name__ == "__main__":
	while True:
		with open(dict_source, 'rb') as f:
			dict_data = pickle.load(f)

		main_request = input("Do you want to compare some word's collocations? If yes, write 'collocations'. If you want to see all available collocations with a word write 'word'. Or write 'exit' if you want to go out. ")
		if main_request in choice_answer_collocations:
			#show_vocabulary = sorted(list(dict_data))
			print("You can see the full list of available words and categories below: ")

			for names in sorted(list(dict_data)):
				print(names, end=' ')
				for categ in sorted(list(dict_data[names])):
					print(categ, end=' ')
				print('\n')

			number_of_words = int(input("Write the the NUMBER of comparing words: "))
			words_category = input("Write the the CATEGORY of comparing words: ")
			word = ''
			comparing_dict = {}
			result_dict = {}
			directory = 'results'
			result_file_name = 'results.txt'

			if number_of_words > 1:
				check_in = Check(words_category)
				if check_in.check_type(words_category) == 1:

					comparing_category = input("Write the COMPARING CATEGORY: ")
					check_in = Check(comparing_category)
					if check_in.check_type(comparing_category) == 1:

						for i in range(0, number_of_words):
							k = i+1
							word = input(f"Write the word number {k}: ")
							if check_in.check_w(word) == 1:
								if word in dict_data.keys():
									if words_category in dict_data[word]:							
										if comparing_category in dict_data[word][words_category]['collocations']:
											if word not in comparing_dict.keys():
												if len(comparing_dict) != 0:
													comparing_dict_of_one_word = {}
													comparing_dict_of_one_word[word] = {}
													comparing_dict_of_one_word[word][comparing_category] = dict_data[word][words_category]['collocations'][comparing_category]
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
													comparing_dict[word][comparing_category] = dict_data[word][words_category]['collocations'][comparing_category]
													result_file_name = word + '_' + result_file_name
													#print(comparing_dict[word][comparing_category])
											else:
												print("You've already typed that word.")
										else:
											print(error_category_message)
									else:
										print(error_category_message)				
								else:
									print(error_message)
									break
						#сформировали имя файла						
						#сформировали словарь по ключевым словам с БД

						if len(comparing_dict) > 1:
							print(result_file_name)
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
							print("You just have a word. There is no need to save that. Try again! ")

			else:
				print("It's not a number. Restart the program and try again. ")
				break
		elif main_request in choice_answer_word:
			word = input(name_input)
			result_dict = {}
			directory = 'results'
			result_file_name = 'results.txt'

			check_in = Check(word)
			if check_in.check_w(word) == 1:
				for i in dict_data.keys():
					if i == word:
						#print(f"{i} is {word} in dict")
						#13.10.2023 {'n + n_after', 'adv + v', 'adj + n', 'v + n', 'adj + n_after', 'n + n', 'adv + adj', 'adj + v', 'phr_v + n_after', 'n + v', 'v + n_after', 'phr_v + n'}
						for k in dict_data[i].keys():
							for o in dict_data[i][k]:
								if o == 'collocations':
									for l in dict_data[i][k][o].keys():
										if k == 'adj' and l == 'n':
											for n in sorted(list(dict_data[i][k][o][l])):
												print(word, n)
										if k == 'v' and l == 'n':
											for n in sorted(list(dict_data[i][k][o][l])):
												print(word, n)
										if k == 'n' and l == 'v':
											for n in sorted(list(dict_data[i][k][o][l])):
												print(word, n)
										if k == 'phr_v' and l == 'n':
											for n in sorted(list(dict_data[i][k][o][l])):
												print(word, n)
										if k == 'adv' and l == 'v':
											for n in sorted(list(dict_data[i][k][o][l])):
												print(n, word)
										if k == 'adv' and l == 'adj':
											for n in sorted(list(dict_data[i][k][o][l])):
												print(word, n)
										if k == 'n' and l == 'n':
											for n in sorted(list(dict_data[i][k][o][l])):
												print(word, n)
										if k == 'n' and l == 'n_after':
											for n in sorted(list(dict_data[i][k][o][l])):
												print(n, word)
										if k == 'adj' and l == 'n_after':
											for n in sorted(list(dict_data[i][k][o][l])):
												print(n, word)
										if k == 'v' and l == 'n_after':
											for n in sorted(list(dict_data[i][k][o][l])):
												print(n, word)
										if k == 'phr_v' and l == 'n_after':
											for n in sorted(list(dict_data[i][k][o][l])):
												print(n, word)
					if i != word:
						for k in dict_data[i].keys():
							for o in dict_data[i][k]:
								if o == 'collocations':
									for l in dict_data[i][k][o].keys():
										if word in tuple(dict_data[i][k][o][l]):
											if k == 'adj' and l == 'n':
												print(i, word)
											if k == 'v' and l == 'n':
												print(i, word)
											if k == 'n' and l == 'v':
												print(i, word)
											if k == 'phr_v' and l == 'n':
												print(i, word)
											if k == 'adv' and l == 'v':
												print(word, i)
											if k == 'adv' and l == 'adj':
												print(i, word)
											if k == 'n' and l == 'n':
												print(i, word)
											if k == 'n' and l == 'n_after':
												print(word, i)
											if k == 'adj' and l == 'n_after':
												print(word, i)
											if k == 'v' and l == 'n_after':
												print(word, i)
											if k == 'phr_v' and l == 'n_after':
												print(word, i)
											#13.10.2023 {'n + n_after', 'adv + v', 'adj + n', 'v + n', 'adj + n_after', 'n + n', 'adv + adj', 'adj + v', 'phr_v + n_after', 'n + v', 'v + n_after', 'phr_v + n'}

		else:
			break
