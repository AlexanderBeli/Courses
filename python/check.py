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