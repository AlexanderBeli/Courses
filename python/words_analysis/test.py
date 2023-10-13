import pickle

dict_source = 'eng_dict.pickle'
with open(dict_source, 'rb') as f1:
	dict_data = pickle.load(f1)

print(dict_data['premature'])