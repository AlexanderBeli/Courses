dict_data = {'word' : {'meaning' : {'n' : '123'}}}
extra_info = 'n'
dict_data['word']['meaning'].pop(extra_info)
print(dict_data)