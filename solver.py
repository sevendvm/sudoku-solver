
# field = [[0 for i in range(0, 9)] for j in range(0, 9)]


class Field:
	def __init__(self):
		self.emptyCells = 9*9
		self.field = [[0 for i in range(0, 9)] for j in range(0, 9)]
		self.possibleNumbers = [[[k for k in range(1, 10)] for i in range(0, 9)] for j in range(0, 9)]
		self.any_solutions_round = False
	
	def __str__(self):
		res = '\n'.join((self.field[i].__str__() for i in range(0, 9)))
		return res
		
	def setup_field(self):
		# self.field = \
		# [[5,3,0,0,7,0,0,0,0],
		#  [6,0,0,1,9,5,0,0,0],
		#  [0,9,8,0,0,0,0,6,0],
		#  [8,0,0,0,6,0,0,0,3],
		#  [4,0,0,8,0,3,0,0,1],
		#  [7,0,0,0,2,0,0,0,6],
		#  [0,6,0,0,0,0,2,8,0],
		#  [0,0,0,4,1,9,0,0,5],
		#  [0,0,0,0,8,0,0,7,9]]
	
		# self.field = \
		# [[0,3,0,5,0,8,0,7,0],
		#  [7,0,0,0,0,0,0,0,5],
		#  [6,0,5,0,9,0,8,0,3],
		#  [0,4,0,7,0,9,0,6,0],
		#  [0,0,0,4,0,5,0,0,0],
		#  [0,9,0,6,0,2,0,3,0],
		#  [2,0,4,0,7,0,6,0,8],
		#  [3,0,0,0,0,0,0,0,2],
		#  [0,8,0,2,0,4,0,5,0]]
		
		# self.field = \
		#  [[0, 8, 0, 0, 0, 0, 0, 2, 0],
		#   [0, 0, 0, 4, 7, 5, 0, 0, 0],
		#   [3, 0, 0, 0, 0, 0, 0, 0, 4],
		#   [0, 0, 8, 0, 4, 0, 2, 0, 0],
		#   [0, 1, 0, 5, 0, 9, 0, 4, 0],
		#   [0, 0, 2, 0, 1, 0, 6, 0, 0],
		#   [9, 0, 0, 0, 0, 0, 0, 0, 3],
		#   [0, 0, 0, 3, 6, 4, 0, 0, 0],
		#   [0, 4, 0, 0, 0, 0, 0, 1, 0]]
		
		self.field = \
		 [[1, 8, 0, 0, 0, 0, 0, 4, 2],
		  [4, 0, 6, 0, 0, 0, 5, 0, 1],
		  [0, 3, 5, 0, 0, 0, 9, 6, 0],
		  [0, 0, 0, 1, 4, 9, 0, 0, 0],
		  [0, 0, 0, 7, 0, 3, 0, 0, 0],
		  [0, 0, 0, 5, 2, 6, 0, 0, 0],
		  [0, 7, 2, 0, 0, 0, 8, 5, 0],
		  [5, 0, 8, 0, 0, 0, 1, 0, 3],
		  [6, 1, 0, 0, 0, 0, 0, 7, 4]]
		
		self.update_empty_cells()
		self.update_all_possible_numbers()
		# for i in range(0, 9):
		# 	for j in range(0, 9):
		# 		if self.field[i][j] > 0:
		# 			self.emptyCells -= 1

	def update_empty_cells(self):
		emptyCells = 0
		for i in range(0, 9):
			for j in range(0, 9):
				if self.field[i][j] == 0:
					emptyCells += 1
		self.emptyCells = emptyCells
	
	def check(self):
		correct = True
		for row in range(0, 9):
			numbers = []
			for col in range(0, 9):
				if self.field[row][col] > 0:
					correct = correct and (self.field[row][col] not in numbers)
					if not correct:
						return False
					numbers.append(self.field[row][col])
			
		for col in range(0, 9):
			numbers = []
			for row in range(0, 9):
				if self.field[row][col] > 0:
					correct = correct and (self.field[row][col] not in numbers)
					if not correct:
						return False
					numbers.append(self.field[row][col])
		
		for vcell in range(0, 3):
			for hcell in range(0, 3):
				numbers = []
				for i in range(hcell * 3, hcell * 3 + 3):
					for j in range(vcell * 3, vcell * 3 + 3):
						if self.field[i][j] > 0:
							correct = correct and (self.field[i][j] not in numbers)
							if not correct:
								return False
							numbers.append(self.field[i][j])
		
		return correct
	
	def update_all_possible_numbers(self):
		for row in range(0, 9):
			for col in range(0, 9):
				self.get_possible_numbers_at_cell(row, col)
	
	def get_possible_numbers_at_cell(self, row_index, col_index):
		
		if self.field[row_index][col_index] > 0:
			self.possibleNumbers[row_index][col_index] = []
			return []
		
		possible = self.possibleNumbers[row_index][col_index].copy()  # [i for i in range(1, 10)]
		
		# check one column
		for col in range(0, 9):
			num = self.field[row_index][col]
			if num > 0 and num in possible:
				# print(f'{num} excluded out of columns')
				possible.remove(num)
				if len(possible) == 0:
					self.possibleNumbers[row_index][col_index] = []
					
					if self.field[row_index][col_index] == 0:
						print(f'WARNING. Cell [{row_index, col_index}] is empty so as possible numbers list is')
					
					return []
		
		# check one row
		for row in range(0, 9):
			num = self.field[row][col_index]
			if num > 0 and num in possible:
				# print(f'{num} excluded out of rows')
				possible.remove(num)
				if len(possible) == 0:
					self.possibleNumbers[row_index][col_index] = []
					
					if self.field[row_index][col_index] == 0:
						print(f'WARNING. Cell [{row_index, col_index}] is empty so as possible numbers list is')
					
					return []
		
		# check a cell
		hcell = row_index // 3
		vcell = col_index // 3
		for i in range(hcell * 3, hcell * 3 + 3):
			for j in range(vcell * 3, vcell * 3 + 3):
				num = self.field[i][j]
				if num > 0 and num in possible:
					# print(f'{num} excluded out of cell [{hcell}, {vcell}]')
					possible.remove(num)
					if len(possible) == 0:
						self.possibleNumbers[row_index][col_index] = []
						
						if self.field[row_index][col_index] == 0:
							print(f'WARNING. Cell [{row_index, col_index}] is empty so as possible numbers list is')
						
						return []
		
		# print(f'Not 100% sure. Possible numbers are {possible}') if len(possible) > 1 else\
		# 	print(f'Found single possibility: {possible[0]}')
		self.possibleNumbers[row_index][col_index] = possible.copy()
		return possible
	
	def print_all_possibilities(self, include_empty=False):
		for i in range(0, 9):
			for j in range(0, 9):
				if self.field[i][j] == 0 or include_empty:
					v = self.possibleNumbers[i][j]
					print(f'Possible variants for [{i},{j}] are {v.__str__()}')
	
	def solve(self):
		
		def check_directly_assignable():
			any_changes = False
			for row in range(0, 9):
				for col in range(0, 9):
					if self.field[row][col] == 0:
						# possibilities = self.get_possible_numbers_at_cell(row, col)
						# if len(possibilities) == 1:
						if len(self.possibleNumbers[row][col]) == 1:
							# print(f'[{row},{col}] is set to {possibilities[0]}')
							# self.field[row][col] = possibilities[0]
							print(f'[{row},{col}] is set to {self.possibleNumbers[row][col][0]}')
							self.field[row][col] = self.possibleNumbers[row][col][0]
							self.possibleNumbers[row][col] = []
							self.emptyCells -= 1
							any_changes = True
			return any_changes
		
		self.print_all_possibilities()
		
		# 0. set all cells which have a single possible number
		print('Checking directly assignable cells:')
		iteration = 0
		while check_directly_assignable():
			iteration += 1
			# print(f'=== ITERATION {iteration} COMPLETE ===')
		print(f'Cells to go {self.emptyCells}')
		
		print('RETURNING')
		return False
		
		if self.emptyCells == 0:
			return self.check()
		
		def try_variant(row, col, value):
			self.field[row][col] = value
			self.emptyCells -= 1
			
			self.possibleNumbers[row][col].remove(value)
			
			if self.emptyCells == 0:
				return self.check()
			else:
				sudoku = Field()
				sudoku.field = self.field.copy()
				sudoku.emptyCells = self.emptyCells
				sudoku.possibleNumbers = self.possibleNumbers.copy()
				
				
				
				
				if sudoku.solve():
					return sudoku.check()
					# self.field = sudoku.field
					# self.emptyCells = sudoku.emptyCells
					# self.possibleNumbers
				else:
					self.field[row][col] = 0
					self.emptyCells += 1
		
		# 1. pick an empty cell
		for row in range(0, 9):
			for col in range(0, 9):
				if self.field[row][col] == 0:
					# 2. pick a number
					for candidate in self.possibleNumbers[row][col]:
						print(f'Trying {candidate} at [{row},{col}]')
						if not try_variant(row, col, candidate):
							print('Doesn\'t fit. Continuing...')
							continue
						elif self.emptyCells == 0:
							print('Solution found. Exiting recursion')
							return self.check()
		
		# 3. check if it fits
		# 3.1. if not - break
		# 3.2. if it does
		# 3.2.1 check whether it was the last empty cell
		# 3.2.1.1 if it so - solution found
		# 3.2.1.2 if not - recurse to step 1
		print('Finishing solve')
		return False
	
	def solve_v2(self):
		# Optimizing
		def check_directly_assignable():
			any_changes = False
			for row in range(0, 9):
				for col in range(0, 9):
					if self.field[row][col] == 0:
						# possibilities = self.get_possible_numbers_at_cell(row, col)
						# if len(possibilities) == 1:
						if len(self.possibleNumbers[row][col]) == 1:
							# print(f'[{row},{col}] is set to {possibilities[0]}')
							# self.field[row][col] = possibilities[0]
							print(f'[{row},{col}] is set to {self.possibleNumbers[row][col][0]}')
							self.field[row][col] = self.possibleNumbers[row][col][0]
							self.possibleNumbers[row][col] = []
							self.emptyCells -= 1
							any_changes = True
			return any_changes
		
		# self.print_all_possibilities()
		
		# 0. set all cells which have a single possible number
		print('Checking directly assignable cells:')
		iteration = 0
		while check_directly_assignable():
			iteration += 1
		# print(f'=== ITERATION {iteration} COMPLETE ===')
		print(f'Cells to go {self.emptyCells}')
		
		# There is no more directly assignable cells
		# continuing with guessing
		def solve_internal():
			for row in range(9):
				for col in range(9):
					if self.field[row][col] == 0:
						for candidate in self.possibleNumbers[row][col]:  # self.get_possible_numbers_at_cell(row, col):
							self.field[row][col] = candidate
							# self.possibleNumbers[row][col].remove(candidate)
							self.emptyCells -= 1
							# print(f'Trying {candidate} at [{row}, {col}]')
							
							if self.check():
								if self.emptyCells == 0:
									print('Solution found')
									print(self)
									self.any_solutions_round = True
									return True
								else:
									# self.solve_v2()
									solve_internal()
							else:
								# print(f'Declined {candidate} at [{row}, {col}]')
								self.field[row][col] = 0
								self.emptyCells += 1
						
						self.field[row][col] = 0
						self.emptyCells += 1
						return False
		
		return solve_internal()


def main():
	sudoku = Field()
	sudoku.setup_field()
	
	print('Given a field...')
	print(sudoku)
	
	print(f'Cells to fill in so far: {sudoku.emptyCells}')
	# sudoku.print_all_possibilities()
	
	print('Solving...')
	sudoku.solve_v2()
	if not sudoku.any_solutions_round:
		print('No solutions found.')
	
	if not sudoku.check():
		print('Inconsistent state detected')


if __name__ == '__main__':
	main()

