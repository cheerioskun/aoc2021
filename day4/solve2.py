import re
class Board:
	def __init__(self):
		self.grid = [[0]*5]*5
		self.marked = [[False for i in range(5)] for j in range(5)]
	def setGrid(self, grid):
		self.grid = grid
	def mark(self, x):
		for i in range(5):
			for j in range(5):
				if self.grid[i][j] == x:
					self.marked[i][j] = True
	def isDoneRow(self):
		for i in range(5):
			if all(self.marked[i]):
				return True
		return False
	def isDoneColumn(self):
		for j in range(5):
			if all([self.marked[i][j] for i in range(5)]):
				return True
		return False
	def isDone(self):
		return (self.isDoneRow() or self.isDoneColumn())
	def score(self, lastCalled):
		s = 0
		for i in range(5):
			for j in range(5):
				s += self.grid[i][j] * (not self.marked[i][j])
		return s * lastCalled

with open("input.txt") as f:
	lines = [re.split(r'\s+', x.strip()) for x in f.readlines() if x != '\n']
	N = (len(lines) - 1)//5
	boards = [Board() for i in range(N)]
	for i in range(N):
		grid = [[int(y) for y in x] for x in [lines[5*i + j + 1] for j in range(5)]]
		boards[i].setGrid(grid)
	nums = [int(x) for x in lines[0][0].split(',')]
	won=set()
	for num in nums:
		if len(won) == N:
			exit()
		for i in [x for x in range(N) if x not in won]:
			boards[i].mark(num)
			if boards[i].isDone():
				won.add(i)
				print(boards[i].score(num))
