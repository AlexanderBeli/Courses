import json

with open('eng_dict.json','r',encoding='utf-8') as f:
	dict_eng = json.load(f, object_pairs_hook=lambda n: n.__dir__)

print(type(dict_eng))