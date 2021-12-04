from collections import Counter
with open("input.txt") as f:
	nums = [x.strip() for x in f.readlines()]
	print(nums[:5])
	m = [[x[i] for x in nums] for i in range(len(nums[0]))]
	gamma = ''.join([Counter(x).most_common()[0][0] for x in m])
	print(gamma)
	epsilon = ''.join(['1' if x == '0' else '0' for x in gamma])
	print(epsilon)
	pc = int(gamma, 2) * int(epsilon, 2)
	print(pc)
