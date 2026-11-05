# Move to specific coordinates
def moveTo(coord):
	# coord: Tuple for coordinates (x, y)
	x = get_pos_x()
	y = get_pos_y()


	dX = 0
	dY = 0

	ns = North
	ew = East

	if x > coord[0]:
		dX = (x - coord[0])
		ew = West
	else:
		dX = (coord[0] - x)
		ew = East


	if y > coord[1]:
		dY = (y - coord[1])
		ns = South
	else:
		dY = (coord[1] - y)
		ns = North

	for x in range(dX):
		move(ew)

	for y in range(dY):
		move(ns)


# Track Relative Motion for Maze Solving
DIRECTIONS = [North, East, South, West]
DIRECTION = 0

def getForward():
	return DIRECTIONS[DIRECTION]
	
def getBackward():
	return DIRECTIONS[(DIRECTION + 2) % 4]
	
def getRight():
	return DIRECTIONS[(DIRECTION + 1) % 4]
	
def getLeft():
	return DIRECTIONS[(DIRECTION - 1) % 4]

def moveForward(n = 1, block = True):
	success = True
	for i in range(n):
		success = success and move(getForward())
	return success
		
def moveBackwards(n = 1, block = True):
	success = True
	for i in range(n):
		success = success and move(getBackward())
	return success
		
def moveRight(n = 1, block = True):
	success = True
	for i in range(n):
		success = success and move(getRight())
	return success

def moveLeft(n = 1, block = True):
	success = True
	for i in range(n):
		success = success and move(getLeft())
	return success
	
def turnRight(n = 1):
	global DIRECTION
	DIRECTION = (DIRECTION + n) % 4
	
def turnLeft(n = 1):
	global DIRECTION 
	DIRECTION = (DIRECTION - n) % 4