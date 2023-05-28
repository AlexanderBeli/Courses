#for i in range (1,100,+2):
#	print(i)s
for i in range(1, 100):
	c = 0
	for j in range(2, i):
		if i % j == 0:
			c += 1
	if c != 0:
		print( i, " Делится ", c, "раз.")
	if c == 0:
		print(i)