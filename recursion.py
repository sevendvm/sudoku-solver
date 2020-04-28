import random


def get_value():
	return random.randint(0, 10)


def recurse(depth):
	global variable
	
	variable += 1
	
	print(variable)
	
	if depth == 5:
		return
	else:
		recurse(depth+1)


variable = 1

recurse(0)
