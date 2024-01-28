num = input("Son kiriting: ")

wood_nums = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def woodmatch(num):
	match_count = 0
	for n in num:
		match_count += wood_nums[int(n)]

	return match_count
	