def bubble_sort(arr):
	# x will be both the index point at which we start our sort
	x = 0
	iterations = 1
	switches = -1
	length = len(arr)
	while switches != 0:
		print('iteration: ', iterations, arr)
		x = 0
		while x < length - iterations:
			switches = 0
			if arr[x] > arr[x + 1]:
				arr[x], arr[x + 1] = arr[x + 1], arr[x]
				switches += 1
			x += 1
		iterations += 1
	return (arr, iterations - 1)


s = bubble_sort([1,2,3,4,5])
x = bubble_sort([14,-2,30,-4,5])