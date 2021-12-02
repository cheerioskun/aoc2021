with open("input.txt") as f:
	content = [x.strip().split(' ') for x in f.readlines()]
	print(content[:5])
	p = 0
	d = 0
	for i in content:
		if i[0] == 'forward':
			p += int(i[1])
		if i[0] == 'up':
			d -= int(i[1])
		if i[0] == 'down':
			d += int(i[1])
	print(p, d, p*d)

