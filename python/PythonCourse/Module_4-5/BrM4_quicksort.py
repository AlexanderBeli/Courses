def quicksort(array):
	left = []
	right = []

	if len(array) > 1:
		center = array.pop(len(array) // 2)

		for x in array:
			if x < center:
				left.append(x)

			elif x >= center:
				right.append(x)

		return quicksort(left) + [center] + quicksort(right)

	else:
		return array

a = [ 100, 99, 1, 75, 23, 104, 23,2 , 1, 12, 0]

print(quicksort(a))