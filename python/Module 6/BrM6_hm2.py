'''
Напишите функцию, get_html(link), которая принимает один аргумент - название веб страницы.
Функция должна получать текст веб страницы с помощью библиотеки requests.
def get_html(link):
  pass
Запустите 5 потоков с с данной функцией и разными именами в качестве аргументов.
Сравните время работы параллельного и последовательного запуска с помощью библиотеки time.
Это задание на самостоятельность, где понадобится установка request.
'''
import time
import requests
from threading import Thread

def get_html(link):
	response = requests.get(link)
	print(response.text)

data_url = [
	'https://dzen.ru',
	'https://mail.ru',
	'https://www.yahoo.com',
	'https://www.bbc.com',
	'https://edition.cnn.com'
]


#последовательный формат
d = time.time()

for i in data_url:
	get_html(i)

d2 = time.time() - d

#параллельный формат
c = time.time()

threads = [Thread(target = get_html, args = (link, )) for link in data_url]

for t in threads:
	t.start()
for t in threads:
	t.join()

c2 = time.time() - c

print(d2)
print(c2)


