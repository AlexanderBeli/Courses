#наблюдения с метеостанции
observations = [-10, 3, -7, 0, -4, 5, -2, 0]

for obs in observations:
	if obs > 0:
		print(obs)

for i in range (0, len(observations)):
	if observations[i] > 0:
		print(observations[i])

diff_observations = []
for i in range(1, len(observations)):
	diff = abs(observations[i] - observations[i - 1])
	diff_observations.append(diff)

print(diff_observations)

for i, val in enumerate(observations):
	print(i, val)

y = [i for i in observations if i < 0]
print(y)