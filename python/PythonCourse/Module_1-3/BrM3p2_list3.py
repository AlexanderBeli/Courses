s = "hello, what's your name?"
word_list = s.split()
print(word_list)

new_word_list = []

for i,a in enumerate(word_list):
	a = a.replace('hello', '')
	a = a.replace(',', ' ')
	a = a.replace("'",' ')
	a = a.replace('  ', ' ')
	new_word_list.append(a)
	print(i,a)

print(new_word_list)
new_s = s.replace('hello', ' ')
print(new_s)
new_s = new_s.replace(',', ' ')
print(new_s)