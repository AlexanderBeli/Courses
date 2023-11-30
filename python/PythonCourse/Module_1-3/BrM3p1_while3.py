x = 5
ans = 0

while x != ans:
	ans = int(input())
	if x == ans:
		print('Win')
	elif x>ans:
		print('Need more')
	else:
		print('Need less')