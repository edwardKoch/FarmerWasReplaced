from time_py import *
from motion_py import *
from farmTypes_py import *
from farm_py import *
from farming_py import *
from path_py import manhattanDistance

STEPS_B4_HELP = 50
STEPS_B4_GIVEUP = get_world_size() * get_world_size() * 2
		
# Generate the Maze
# Find the Treasure
# harvest & Destroy Maze
def createAndSolveMaze(x = MAZE_X, y = MAZE_Y, size = MAZE_DIM, depth = 4):
	moveToCoords(x, y)
	# No Fertilizer, No Waiting, No Water, Force Harvest
	harvestAndPlant(BUSH, False, False, False, True)
	# WEIRD Cost scales with upgrade
	use_item(WEIRD, size * get_cost(HEDGE)[WEIRD])
	findTreasureWallFollow(depth)
	# Get the target Coordinates and flood fill
	#floodFillSolver(size, (x, y), measure())
	

# Navigate the Maze
def findTreasureWallFollow(depth):
	# Attempt to spawn a reverse helper
	spawn_drone(leftWallMethod, depth - 1)
	# Traverse the right-wall way
	rightWallMethod(depth - 2)
	
# Follow the right wall until Treasure
def rightWallMethod(depth):
	# Prevent too many drone helpers
	if depth <= 0:
		return
		
	count = 0
	while get_entity_type() != TREASURE and count < STEPS_B4_GIVEUP:
		count += 1
		# If somehow we are out of the maze
		if get_entity_type() != HEDGE:
			break
			
		if count % STEPS_B4_HELP == 0:
			# Attempt to spawn a reverse helper
			spawn_drone(leftWallMethod, depth - 1)
			
		if can_move(getRight()):
			turnRight()
			moveForward()
		elif can_move(getForward()):
			moveForward()
		else:
			turnRight()
			turnRight()
			
	if get_entity_type() == TREASURE:
		harvest()
			
# Follow the left wall until Treasure
def leftWallMethod(depth):
	# Prevent too many drone helpers
	if depth <= 0:
		return
		
	count = 0
	while get_entity_type() != TREASURE and count < STEPS_B4_GIVEUP:
		count += 1
		# If somehow we are out of the maze
		if get_entity_type() != HEDGE:
			break
			
		if count % STEPS_B4_HELP == 0:
			# Attempt to spawn a reverse helper
			spawn_drone(rightWallMethod, depth - 1)
			
		if can_move(getLeft()):
			turnLeft()
			moveForward()
		elif can_move(getForward()):
			moveForward()
		else:
			turnLeft()
			turnLeft()
			
	if get_entity_type() == TREASURE:
		harvest()

# Repeatedly solve mazes
def mazeWorker(conditionFcn, x = MAZE_X, y = MAZE_Y, size = MAZE_DIM):
	while conditionFcn():
		createAndSolveMaze(x, y, size)

def megaMaze(conditionFcn):
	_dim = get_world_size()
	startX, startY = 0, 0
	while conditionFcn():
		createAndSolveMaze(startX, startY, _dim, _dim)

def spamMazes(conditionFcn):
	def mazeSpammer(coord, size, main):	
		moveTo(coord)
		while conditionFcn():
			entity = get_entity_type()
			if entity == TREASURE:
				harvest()
			elif main and entity == GRASS:
				harvestAndPlant(BUSH, False, False, False, True)
				# WEIRD Cost scales with upgrade
				use_item(WEIRD, size * get_cost(HEDGE)[WEIRD])

	_dim = 5
	centerX = 2
	centerY = 2

	cX, cY = centerX, centerY
	center = (cX, cY)

	for x in range (_dim):
		for y in range(_dim):
			if x == cX and y == cY:
				continue
			else:
				spawn_drone(mazeSpammer, (x, y), _dim, False)

	moveTo(center)

	harvestAndPlant(BUSH, False, False, False, True)
	use_item(WEIRD, 3 * get_cost(HEDGE)[WEIRD])

	mazeSpammer(center, _dim, True)


### Flood Fill Algorithms ###

# Generate the cost matrix for the current state of the map
# BFS from target backwards to all nodes
# Target: Target Coordinates
# Size: Dimension of the maze
# Walls: 2D array of list of neighbors that are walled off
def getCostMatrix(target, size, walls):
	# Track distance Grid
	# 2D array of distance to the goal
	distanceGrid = []
	for x in range(size):
		distanceGrid.append([])
		for y in range(size):
			distanceGrid[x].append(-1)

	targX, targY = target

	# Obvi there is 0 cost to get to target from target
	distanceGrid[targX][targY] = 0

	# Initialize queue with target
	bfsQueue = [(targX, targY, 0)]

	qPointer = 0

	# Do BFS
	while qPointer < len(bfsQueue):
		# Get current coord and distance from target
		curX, curY, steps = bfsQueue[qPointer]
		qPointer += 1

		# Check in all 4 directions
		for dir in DIRECTION_OFFSET:
			xOff, yOff = DIRECTION_OFFSET[dir]
			neighborX = curX + xOff
			neighborY = curY + yOff

			# Stay within the grid boundaries
			if 0 <= neighborX < size and 0 <= neighborY < size:
				# Check if any walls already exists
				neighbor = (neighborX, neighborY)
				if neighbor not in walls[curX][curY]:
					# Check if the neighbor is un-visited
					if distanceGrid[neighborX][neighborY] == -1:
						# Log the distance of the neighbor, add to queue to visit
						distanceGrid[neighborX][neighborY] = steps + 1
						bfsQueue.append((neighborX, neighborY, steps + 1))

	return distanceGrid

# Update the cost matrix for local cells only
# ToUpdate: list of coordinates to update
# Costs: Current cost matrix
def updateCostMatrix(toUpdate, costs, walls, size, target):
	qPointer = 0

	# Track which coords are waiting for an update
	inQ = []
	for x in range(size):
		inQ.append([])
		for y in range(size):
			inQ[x].append(False)

	for pos in toUpdate:
		posX, posY = pos
		inQ[posX][posY] = True

	while qPointer < len(toUpdate):
		curPos = toUpdate[qPointer]
		curX, curY = curPos

		inQ[curX][curY] = False
		
		qPointer += 1

		# Target position must always remain at 0
		if curPos == target:
			continue

		# Find the minimum step count of accessible neighbors
		# Move to the neighbor that is closest to the target
		nearestNeighborValue = 9999999999

		# Check in all 4 directions
		for dir in DIRECTION_OFFSET:
			xOff, yOff = DIRECTION_OFFSET[dir]
			neighborX = curX + xOff
			neighborY = curY + yOff

			# Stay within the grid boundaries
			if 0 <= neighborX < size and 0 <= neighborY < size:
				neighbor = (neighborX, neighborY)

				# Check if there is a wall between us
				if neighbor not in walls[curX][curY]:
					cost = costs[neighborX][neighborY]

					if cost != -1 and cost < nearestNeighborValue:
						nearestNeighborValue = cost

		newCost = nearestNeighborValue + 1
		# If the current cell is not lowest neighbor + 1, it is blocked
		# Increment it and add unblocked neighbors to be checked
		if costs[curX][curY] < newCost:
			costs[curX][curY] = newCost

			# Check in all 4 directions
			for dir in DIRECTION_OFFSET:
				xOff, yOff = DIRECTION_OFFSET[dir]
				neighborX = curX + xOff
				neighborY = curY + yOff

				# Stay within the grid boundaries
				if 0 <= neighborX < size and 0 <= neighborY < size:
					neighbor = (neighborX, neighborY)

					# Check if there is a wall between us
					if neighbor not in walls[curX][curY] and not inQ[neighborX][neighborY]:
						toUpdate.append(neighbor)
						inQ[neighborX][neighborY] = True


# Scan the current position for walls
# CurPos: Current Position of Drone
# Size: Dimension of the maze
# Walls: 2D array of list of neighbors that are walled off
# Returns: List of cells affected by a discovered wall
def scanForWalls(curPos, size, walls):
	affectedCells = []

	curX, curY = curPos

	# Check in all 4 directions
	for dir in DIRECTION_OFFSET:
		xOff, yOff = DIRECTION_OFFSET[dir]
		neighborX = curX + xOff
		neighborY = curY + yOff

		# Stay within the grid boundaries
		if 0 <= neighborX < size and 0 <= neighborY < size:
			# Check if any walls already exists
			neighbor = (neighborX, neighborY)

			# Check for a wall
			isWall = not can_move(dir)
			isKnown = neighbor in walls[curX][curY]

			# If this wall is a new wall
			if isWall and not isKnown:
				walls[curX][curY].append(neighbor)
				walls[neighborX][neighborY].append(curPos)
				if curPos not in affectedCells:
					affectedCells.append(curPos)
				if neighbor not in affectedCells:
					affectedCells.append(neighbor)

	return affectedCells

# Solves the maze with Flood Fill
# Size: Dimension of the maze
# Start: Begining Coordinates
# Target: Target Coordinates
def floodFillSolver(size, start, target):
	# Track walls in the farm
	# 2D array of a list of neighbors that are walled off
	discoveredWalls = []
	for x in range(size):
		discoveredWalls.append([])
		for y in range(size):
			discoveredWalls[x].append([])

	# Initialize the cost matrix to all manhattan distances
	costMatrix = []
	for x in range(size):
		costMatrix.append([])
		for y in range(size):
			costMatrix[x].append(manhattanDistance((x, y), target))

	# Track if we have reached the end or not
	curPos = start
	success = curPos == target

	# Solve the Maze
	while not success:
		curX, curY = curPos

		# Update Wall map based on current location
		affectedCells = scanForWalls(curPos, size, discoveredWalls)
		if len(affectedCells) > 0:
			# If the walls changed get the new cost matrix for the maze
			#costMatrix = getCostMatrix(target, size, discoveredWalls)
			updateCostMatrix(affectedCells, costMatrix, discoveredWalls, size, target)

		# Move to the neighbor that is closest to the target
		optimalDir = None
		nearestNeighborValue = 9999999999

		# Check in all 4 directions
		for dir in DIRECTION_OFFSET:
			xOff, yOff = DIRECTION_OFFSET[dir]
			neighborX = curX + xOff
			neighborY = curY + yOff

			# Stay within the grid boundaries
			if 0 <= neighborX < size and 0 <= neighborY < size:
				neighbor = (neighborX, neighborY)

				# Check if there is a known wall between us
				if neighbor not in discoveredWalls[curX][curY]:
					cost = costMatrix[neighborX][neighborY]

					if cost != -1 and cost < nearestNeighborValue:
						optimalDir = dir
						nearestNeighborValue = cost

		# Since this maze is closed, assume there is always a path
		#if optimalDir != None:
		move(optimalDir)
		curPos = (get_pos_x(), get_pos_y())

		# Track if we have reached the end or not
		success = curPos == target

	if get_entity_type() == TREASURE:
		harvest()