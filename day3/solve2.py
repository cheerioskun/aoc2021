from collections import Counter
with open("input.txt") as f:
	nums = [x.strip() for x in f.readlines()]
	print(nums[:5])
	n = len(nums)
	m = len(nums[0])
	a,b = 0,0
	working = set(nums)
	for i in range(m):
		ones = sum([(j[i]=='1') for j in working])
		if ones >= (len(working) + 1)//2:
			working = set([j for j in working if j[i] == '1'])
		else:
			working = set([j for j in working if j[i] == '0'])
		if len(working) == 1:
			a = working.pop()
			print(a)
			a = int(a, 2)
				
	working = set(nums)
	for i in range(m):
		ones = sum([(j[i]=='1') for j in working])
		if ones >= (len(working) + 1)//2:
			working = set([j for j in working if j[i] == '0'])
		else:
			working = set([j for j in working if j[i] == '1'])
		if len(working) == 1:
			b = working.pop()
			print(b)
			b = int(b, 2)
	print(a * b)
