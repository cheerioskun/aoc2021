with open("input.txt") as f:
	nums = [int(x[:-1]) for x in f.readlines()]
	print(nums[:10])
	print(sum([nums[i] > nums[i-1] for i in range(1, len(nums))]))

