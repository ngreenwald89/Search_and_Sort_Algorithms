def quicksort(array):
	x = 1
	len_array = len(array)
	p_idx = len_array - 1
	i = 0
	# code to move pivot into correct spot
	while i < p_idx:
		# print('i', i, 'pivot', p_idx)
		if array[p_idx] < array[i]:
			if i == p_idx - 1:
				# print("i is left of pivot")
				array[p_idx], array[i] = array[i], array[p_idx]
			else:
			 	# pivot moves left one, head takes pivot's spot, left of pivot takes head's spot
				array[p_idx - 1], array[p_idx], array[i] = array[p_idx], array[i], array[p_idx - 1]
			p_idx -= 1
		else:
			# print("i is greater than pivot")
			i += 1
		# print(array)
	else:
		# print("partition complete")	
		if p_idx > 0:
			array[:p_idx] = quicksort(array[:p_idx])
		if array[p_idx + 1:]:
			array[p_idx + 1:] = quicksort(array[p_idx + 1:])
		return array
			

l=[3,4,0,7,-1,-4]
"""
# random lists
import random
# parameters: population, k elements to select from population
r = random.sample(range(n), k)
"""