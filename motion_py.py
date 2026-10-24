from time_py import *

DIRECTIONS = [North, East, South, West]
REVERSE_DIRS = {
	North : South,
	South : North,
	East : West,
	West : East
}
DIRECTION_OFFSET = {
	North : (0, 1),
	South : (0, -1),
	East : (1, 0),
	West : (-1, 0)
}

# Move a direction
# Block: True if drone should try forever to move
def moveIfPossible(dir, block = True):
	if block:
		while not move(dir):
			continue
		return True
	else:
		return move(dir)

# Get the direction from P1 -> P2
# P1, P2: 2 Squares in the same row OR col
# If in different rows and cols, return North
def getDir(p1, p2):
	x1 = p1[0]
	y1 = p1[1]

	x2 = p2[0]
	y2 = p2[1]

	if x1 == x2:
		if y1 < y2:
			return North
		return South

	if y1 == y2:
		if x1 < x2:
			return East
		return West		
		
### ABSOLUTE MOVEMENT
# Move directly to come coordinates
# Block: True if drone should try forever to move
def moveToCoords(x, y, block = True):
	# Track if move succeeded
	success = True
	# Floor ints for determinism
	x = x // 1
	y = y // 1
	
	# Get shortest path on the X Axis
	dir, len = getShortestPath(get_pos_x(), x)
	for i in range(len):
		if dir:
			success = success and moveIfPossible(East, block)
		else:
			success = success and moveIfPossible(West, block)
	
	# Get shortest path on the Y Axis
	dir, len = getShortestPath(get_pos_y(), y)
	for i in range(len):
		if dir:
			success = success and moveIfPossible(North, block)
		else:
			success = success and moveIfPossible(South, block)

	return success

# Move directly to a square
# Block: True if drone should try forever to move
def moveTo(p1, block = True):
	return moveToCoords(p1[0], p1[1], block)

### RELATIVE MOVEMENT
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
		success = success and moveIfPossible(getForward(), block)
	return success
		
def moveBackwards(n = 1, block = True):
	success = True
	for i in range(n):
		success = success and moveIfPossible(getBackward(), block)
	return success
		
def moveRight(n = 1, block = True):
	success = True
	for i in range(n):
		success = success and moveIfPossible(getRight(), block)
	return success

def moveLeft(n = 1, block = True):
	success = True
	for i in range(n):
		success = success and moveIfPossible(getLeft(), block)
	return success
	
def turnRight(n = 1):
	global DIRECTION
	DIRECTION = (DIRECTION + n) % 4
	
def turnLeft(n = 1):
	global DIRECTION 
	DIRECTION = (DIRECTION - n) % 4

### HELPER FUNCTIONS

# Reset to origin
def resetPos():
	moveToCoords(0, 0)
	
# Get the direction and spaces to move in order to move to a new index
# finds shortest path left or right or up or down
# Returns Tuple <Bool, int>
# True if Pos Dir (N/E) False if Neg Dir (S/W)
# Number of spaces to move
def getShortestPath(src, dest):
	# Get how long a direct path would be
	directLength = 0
	directDirection = False
	# If we want to go N or E
	if dest > src:
		directLength = dest - src
		directDirection = True
	# If we want to go S or W
	else:
		directLength = src - dest
		directDirection = False
		
	# Get how long it would be to wrap around
	wrapLength = 0
	wrapDirection = False
	# If we want to go N or E
	if dest > src:
		# Get how far it would be to wrap around S or W
		# Travel S/W for src until wrap, then from MAX to the dest
		wrapLength = src + (get_world_size() - dest)
		wrapDirection = False
	# If we want to go S or E
	else:
		# Get how far it would be to wrap around N or E
		# Travel N/E from src to MAX, then from 0 to dest
		wrapLength = (get_world_size() - src) + dest
		wrapDirection = True
		
	if directLength < wrapLength:
		return directDirection, directLength
	else:
		return wrapDirection, wrapLength
		
		
		
		
		
		
		