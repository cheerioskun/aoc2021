with open("input.txt") as f:
	nums = [int(x[:-1]) for x in f.readlines()]
	print(nums[:10])
	print(sum([nums[i] > nums[i-3] for i in range(3, len(nums))]))

