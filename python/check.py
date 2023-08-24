from random import randint

a = []
for i in range(10):
    a.append(randint(1, 50))

print(a)

#a = [int(x) for x in a]

def sortion_function(a):
#	if i is None:
#		i = -1

#	i += 1 
	pl = len(a)
	for i in range(len(a)):
		sortion_function(a[pl - 1])
		print(sortion_function(a[pl - 1]))
#			if a[i] > a[i+1] and i+1 < (pl -1):
#				a[i], a[i+1] = a[i+1], a[i]
	return a

sortion_function(a)
print(a)