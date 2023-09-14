eng_dict = {}
name = 'significant'

with open('nouns.txt', 'r', encoding='utf-8') as f:
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