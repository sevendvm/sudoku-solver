field = \
	[[1, 8, 0, 0, 0, 0, 0, 4, 2],
	 [4, 0, 6, 0, 0, 0, 5, 0, 1],
	 [0, 3, 5, 0, 0, 0, 9, 6, 0],
	 [0, 0, 0, 1, 4, 9, 0, 0, 0],
	 [0, 0, 0, 7, 0, 3, 0, 0, 0],
	 [0, 0, 0, 5, 2, 6, 0, 0, 0],
	 [0, 7, 2, 0, 0, 0, 8, 5, 0],
	 [5, 0, 8, 0, 0, 0, 1, 0, 3],
	 [6, 1, 0, 0, 0, 0, 0, 7, 4]]

# field = \
# 	[[5, 3, 0, 0, 7, 0, 0, 0, 0],
# 	 [6, 0, 0, 1, 9, 5, 0, 0, 0],
# 	 [0, 9, 8, 0, 0, 0, 0, 6, 0],
# 	 [8, 0, 0, 0, 6, 0, 0, 0, 3],
# 	 [4, 0, 0, 8, 0, 3, 0, 0, 1],
# 	 [7, 0, 0, 0, 2, 0, 0, 0, 6],
# 	 [0, 6, 0, 0, 0, 0, 2, 8, 0],
# 	 [0, 0, 0, 4, 1, 9, 0, 0, 5],
# 	 [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def check():
	correct = True
	for row in range(0, 9):
		numbers = []
		for col in range(0, 9):
			if field[row][col] > 0:
				correct = correct and (field[row][col] not in numbers)
				if not correct:
					return False
				numbers.append(field[row][col])
	
	for col in range(0, 9):
		numbers = []
		for row in range(0, 9):
			if field[row][col] > 0:
				correct = correct and (field[row][col] not in numbers)
				if not correct:
					return False
				numbers.append(field[row][col])
	
	for vcell in range(0, 3):
		for hcell in range(0, 3):
			numbers = []
			for i in range(hcell * 3, hcell * 3 + 3):
				for j in range(vcell * 3, vcell * 3 + 3):
					if field[i][j] > 0:
						correct = correct and (field[i][j] not in numbers)
						if not correct:
							return False
						numbers.append(field[i][j])
	
	return correct


# emptyCells = 47


def get_empty_cells_count(field):
	emptyCells = 0
	for i in range(9):
		for j in range(9):
			if field[i][j] == 0:
				emptyCells += 1
	return emptyCells


emptyCells = get_empty_cells_count(field)


def solve():
	
	global field
	global emptyCells
	
	# print(f'{emptyCells} to go')
	
	for row in range(9):
		for col in range(9):
			if field[row][col] == 0:
				for candidate in range(1, 10):  # possibleNumbers[row][col]:
					field[row][col] = candidate
					# possibleNumbers[row][col].remove(candidate)
					emptyCells -= 1
					# print(f'Trying {candidate} at [{row}, {col}]')
					
					if check():
						if emptyCells == 0:
							print('Solution found')
							print(field)
							return
						else:
							solve()
					else:
						# print(f'Declined {candidate} at [{row}, {col}]')
						field[row][col] = 0
						emptyCells += 1
				
				field[row][col] = 0
				emptyCells += 1
				return


# print('Exited inner loop')


# print('Exited outer loop')
# print(field)

# print(check())
solve()
# print(field)
