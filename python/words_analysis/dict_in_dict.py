import json
import pickle

#добавил категорию 'n' 
'''with open('eng_dict.json','r',encoding='utf-8') as f:
	eng_dict = json.load(f)

for w, v in eng_dict.items():
	print(w)
	adj = {'n':v}
	eng_dict[w] = adj
	print(eng_dict[w], '\n\n')

with open('eng_dict.json','w',encoding='utf-8') as f:
	json.dump(eng_dict, f)'''

#print(eng_dict['key']['n'][2])



#list of words to set of words
for w, v in eng_dict.items():
	for i, k in v.items():
		l = set(k)
		eng_dict[w][i] = l

new_eng_dict = eng_dict
#print(new_eng_dict)
#Object of type set is not JSON serializable

#with open('eng_dict.pickle','wb') as f:
#	pickle.dump(new_eng_dict, f)

with open('eng_dict.pickle','rb') as f:
	pickle_eng_dict = pickle.load(f)

print(pickle_eng_dict)
print(type(pickle_eng_dict))



#add 'meaning'

