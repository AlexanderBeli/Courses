#функция, которая считает площадь треугольника по трем сторонам

def area(a, b, c):
#найдем гипотенузу
	gipo = max(a, b, c)

#выделить два других параметра
	katet1 = min(a, b, c)
	katet2 = a + b + c - gipo - katet1

#вычислить высоту к гипотенузе
#исходя из теоремы Пифагора
	p = a + b + c
	h = 2 * ((p * (p - gipo) * (p - katet1) * (p - katet2)) ** 0.5) / gipo 

#вычислить площадь треугольника
	s = h * gipo / 2
	print(s)

a = int(input('Введите 1ю сторону треугольника '))
b = int(input('Введите 2ю сторону треугольника '))
c = int(input('Введите 3ю сторону треугольника '))

area(a, b, c)


#написать функцию, которая возвращает слова
#текст в файле txt, приложен к файлу
new_list = []

def words_back(content):
	content = content.replace(',', ' ').replace('?', ' ').replace('.', ' ')
	word_list = content.split()

	for i in range(0, len(word_list)):
		if len(word_list[i]) < 5:
			new_list.append(word_list[i])

	print(new_list)



with open('BrM3p4_hm3.txt', 'r', encoding='utf-8') as f:
	content = f.read()

words_back(content)

#написать функцию, которая составляет макс число
list_numbers = [56, 9, 11, 2]

c = []
f = []

def create_number(z):
	for i in range(0, len(z)):
		a = str(z[i])
		b = int(a[0])
		c.append(b)
	
	d = sorted(c)

#	f = z

	for j in range(0, len(z)):
		g = str(z[j])
		h = int(g[0])

		for k in range(0, len(d)):
			if d[k] == h:
				print(g)
#хочу соотнести цифры по первым цифрам в списке d и заменить соответствующие цифры местами
#затем все сделать строкой и убрать запятые

#никак не срабатывает код на замену цифр, соотносить соотносит но в список никак не добавляет

	print(d)


create_number(list_numbers)