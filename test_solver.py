# from unittest import TestCase
#
#
# class TestField(TestCase):
# 	def test_check(self):
# 		self.fail()

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


def check_cell(vcell, hcell):
	# for vcell in range(0, 3):
	# 	for hcell in range(0, 3):
	correct = True
	numbers = []
	for i in range(hcell * 3, hcell * 3 + 3):
		for j in range(vcell * 3, vcell * 3 + 3):
			if field[i][j] > 0:
				correct = correct and (field[i][j] not in numbers)
				if not correct:
					return False
				numbers.append(field[i][j])
	return True

for i in range(3):
	for j in range(3):
		print(f'{i},{j} {check_cell(i,j)}')

# print(check_cell(2, 0))