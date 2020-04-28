class Cell:
	def __init__(self, initial):
		self.cell = [[initial, initial, initial],
					 [initial, initial, initial],
					 [initial, initial, initial]]
	
	def __str__(self):
		res = ''
		for i in range(0, 3):
			res += self.cell[i].__str__() + '\n'
		return res
	
	def check(self):
		pass


class Field:
	def __init__(self):
		self.field = [[Cell(1), Cell(2), Cell(3)],
					  [Cell(4), Cell(5), Cell(6)],
					  [Cell(7), Cell(8), Cell(9)]]
	
	def __str__(self):
		res = ''
		for j in range(0, 3):
			for i in range(0, 3):
				res += self.field[i][j].__str__()
			res += '\n'
		return res
	
	def check(self):
		pass


print(Field())
