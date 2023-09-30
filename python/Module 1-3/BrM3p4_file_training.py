#запишем в файл реккорд Васи

highscore_file = open('highscore.txt', 'w', encoding='utf-8')
highscore_file.write('Вася 100')
highscore_file.close()

highscore_file = open('highscore.txt', 'r')
highscores = highscore_file.read()
highscore_file.close()

with open('highscore.txt', 'r', encoding='utf-8') as file:
	content = file.read()
	print(content)

#add info
with open('highscore.txt', 'a', encoding='utf-8') as file:
	file.write(' level 2')

import json

data = [1, 2, 3]

#with open('1.json', 'w') as f:
#	json.dump(data,f)

with open('1.json', 'r') as f:
	data1 = json.load(f)

print(data1)
