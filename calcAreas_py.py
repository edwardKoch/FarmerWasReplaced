# from areas_py import *
# Manage the different areas of the farm
NE = 0
NNE = 1
ENE = 2
NW = 3
NNW = 4
WNW = 5
SW = 6
WSW = 7
SSW = 8
SE = 9
SSE = 10
ESE = 11
NE_DIAG = 12
NW_DIAG = 13
SW_DIAG = 14
SE_DIAG = 15
NUM_AREAS = 16

INV = 99999

AREAS = {}

# Checks is a coordinate is in a plot
def isInArea(x, y, area):
	dim = 32 # get_world_size()
	
	# NorthEast Quadrant
	if (x >= dim // 2) and (y >= dim // 2):
		if area == NE:
			return True
		elif area == NNE and x < y:
			return True
		elif area == ENE and x > y:
			return True

	# NorthWest Quadrant
	if (x < dim // 2) and (y >= dim // 2):
		if area == NW:
			return True
		elif area == NNW and (dim - 1 - (x + y)) < 0:
			return True
		elif area == WNW and (dim - 1 - (x + y)) > 0:
			return True
	
	# SouthWest Quadrant
	if (x < dim // 2) and (y < dim // 2):
		if area == SW:
			return True
		elif area == SSW and x > y:
			return True
		elif area == WSW and x < y:
			return True
		
	# SouthEast Quadrant
	if (x >= dim // 2) and (y < dim // 2):
		if area == SE:
			return True
		elif area == ESE and (dim - 1 - (x + y)) < 0:
			return True
		elif area == SSE and (dim - 1 - (x + y)) > 0:
			return True
	
	# Positive Diagonal
	if x == y:
		if area == NE_DIAG and (x >= dim // 2):
			return True
		if area == SW_DIAG and (x < dim // 2):
			return True
			
	# Negative Diagonal
	if (dim - 1 - (x + y)) == 0:
		if area == SE_DIAG and (x >= dim // 2):
			return True
		if area == NW_DIAG and (x < dim // 2):
			return True
		
	return False

# Create dict of areas
for area in range(NUM_AREAS):
	AREAS[area] = []
	
dim = 32 # get_world_size()

# Iterate through entire FARM
for x in range(dim):
	for y in range(dim):
		for area in range(NUM_AREAS):
			if isInArea(x, y, area):
				AREAS[area].append((x, y))

#with open("output.txt", "w") as f:
	#print("AREAS = {", sep='',file=f)
	#for key in AREAS:
		#print(key, ':', AREAS[key], ',', sep='',file=f)
	#print('}', sep='',file=f)