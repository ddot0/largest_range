def largestRange(array):
	# use hash
	arrayset = set(array)
	rangecount = 0
	AnsArray = []
	# start with an integer that is in the array
	for n in arrayset:
		# the length of the range begins
		active_rangecount = 1
		# identify the integers that would follow before and after consecutively
		prev_num = n - 1
		next_num = n + 1
		# start to add to length as long as the correct integers are in the array
		while prev_num in arrayset:
			active_rangecount += 1
			prev_num -= 1
		while next_num in arrayset:
			active_rangecount += 1
			next_num += 1
		# identify the largest range between integers in array and return them as array of length 2
		if active_rangecount >= rangecount:
			rangecount = active_rangecount
			AnsArray = [prev_num + 1, next_num - 1]
	return AnsArray