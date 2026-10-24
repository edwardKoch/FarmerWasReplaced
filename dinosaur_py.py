from motion_py import *
from farmTypes_py import *
from hamiltonian_py import *

# Raw Hamiltonian Snake
def playSnake0(zDim):

	resetPos()

	# Equip Dino Hat - Spawns Apple underneath
	change_hat(Hats.Dinosaur_Hat)

	# Generate Looping path without edge rollover
	ableToMove = True
	while ableToMove:
		# Move to top left corner
		for i in range(zDim ):
			ableToMove = ableToMove and moveForward(1, False)

		# move to top right corner
		for i in range(zDim):
			ableToMove = ableToMove and moveRight(1, False)

		# Move down one
		ableToMove = ableToMove and moveBackwards(1, False)

		# ZigZag back down to the first row
		for i in range((zDim // 2)):
			# Left to before the first column
			for i in range(zDim - 1):
				ableToMove = ableToMove and moveLeft(1, False)

			# Move down one
			ableToMove = ableToMove and moveBackwards(1, False)
			
			# Right to the edge
			for i in range(zDim - 1):
				ableToMove = ableToMove and moveRight(1, False)
			
			# Move down one
			ableToMove = ableToMove and moveBackwards(1, False)

		# Left to before the first column
		for i in range(zDim):
			ableToMove = ableToMove and moveLeft(1, False)


	# Equip Default hat- Harvests Tail
	change_hat(Hats.Straw_Hat)

# Raw Hamiltonion Snake - using pre-calculated path
def playSnake1():
		# Go to begining of farm
		resetPos()

		# Equip Dino Hat - Spawns Apple underneath
		change_hat(Hats.Dinosaur_Hat)

		nextX = 0
		nextY = 0

		ableToMove = True
		while ableToMove:
			# Move through Hamiltonian Path
			index = 1
			for dir in HamiltonianDirs:
				# See if we are over an apple
				if get_entity_type() == APPLE:
					# Get next apple coords
					nextX, nextY = measure()

				# Move in the next Direciton
				ableToMove = move(dir)

		# Equip Default hat- Harvests Tail
		change_hat(Hats.Straw_Hat)

def updatePos(curX, curY, dir):
	# Update the CurX/Y
	if dir == South: 
		curY -= 1
	elif dir == North: 
		curY += 1
	elif dir == East: 
		curX += 1
	elif dir == West: 
		curX -= 1

	headPos = (curX, curY)

	return curX, curY, headPos

# Hamiltonion Map Snake - using pre-calculated Map
def playSnake2():
		# Go to begining of farm
		resetPos()

		curX = 0
		curY = 0
		headPos = (curX, curY)

		# Equip Dino Hat - Spawns Apple underneath
		change_hat(Hats.Dinosaur_Hat)

		nextX = 0
		nextY = 0

		ableToMove = True
		while ableToMove:
			# Get the direciton to move next
			dir = HamiltonianCoordToDirMap[headPos]

			# See if we are over an apple
			if get_entity_type() == APPLE:
				# Get next apple coords
				nextX, nextY = measure()

			# Move in the next Direciton
			ableToMove = move(dir)

			# Update the headPos
			curX, curY, headPos = updatePos(curX, curY, dir)

		# Equip Default hat- Harvests Tail
		change_hat(Hats.Straw_Hat)

# Hamiltonion Array Snake - with Shortcuts - Phase optimization
def playSnake():

	# 64 is 2 rows of snake, low likelyhood of colisions
	GreedyThreshold = 70
	# 256 is 25% of the map, low likelyhood of finding shortcuts
	BruteThreshold = 375

	# Go to begining of farm
	resetPos()

	# Track position
	curX = 0
	curY = 0

	# Track Body Position
	# Use circular buffer to reduce size and lookup time
	# NullBodyBuffer is 1024 (-1, -1) in a list
	bodyBuffer = NullBodyBuffer
	bufferLen = 1024
	bodyLen = 1

	headIdx = 0
	bodyBuffer[headIdx] = (curX, curY)

	# Equip Dino Hat - Spawns Apple underneath
	change_hat(Hats.Dinosaur_Hat)

	nextX, nextY = measure()

	# Phase 1: Unsafe Shortcuts
	# For short snakes, use the apple shortcuts without tail checks
	# The tail is too short to matter
	while bodyLen < GreedyThreshold:
		# Get the direciton to move next
		dir = HamiltonianCoordToDirArr[curX][curY]

		# See if we are over the apple coordinates
		if curX == nextX and curY == nextY:
			# Get next apple coords
			nextX, nextY = measure()
			# Body will grow on move
			bodyLen += 1

		# Move in the next Direciton
		move(dir)

		# Update the headPos
		dx, dy = DIRECTION_OFFSET[dir]
		curX += dx
		curY += dy

		# Check if  the apple is more than 1 zig/zag below 
		if dir != North and (nextY + 2) < curY:
			# Cut down until we are in the closest zig/zag to the apple
			while (nextY + 1) < curY:
				move(South)
				# Update the headPos
				curY -= 1

		# If the apple is above us
		elif dir != North and nextY > curY:
			# Cut down to the bottom of the map
			while curY > 0:
				move(South)
				# Update the headPos
				curY -= 1
			# Cut back to the starting point
			while curX > 0:
				move(West)
				# Update the headPos
				curX -= 1

	# Phase 2: Use smart shortcuts
	# Track the Tail to ensure no collisions
	while bodyLen < BruteThreshold:
		# Get the direciton to move next
		dir = HamiltonianCoordToDirArr[curX][curY]

		# See if we are over the apple coordinates
		if curX == nextX and curY == nextY:
			# Get next apple coords
			nextX, nextY = measure()
			# Body will grow on move
			bodyLen += 1

		# Move in the next Direciton
		move(dir)

		# Update the headPos
		dx, dy = DIRECTION_OFFSET[dir]
		curX += dx
		curY += dy

		headIdx = (headIdx + 1) % bufferLen
		bodyBuffer[headIdx] = (curX, curY)

		# Check if we just moved south - row transition
		if dir == South:

			# And the apple is more than 1 zig/zag below 
			if (nextY + 2) < curY:

				tailIdx = (headIdx - bodyLen + 1) % bufferLen
				tailPos = bodyBuffer[tailIdx]

				# Check if the tail is to the north of us or south of the apple
				if tailPos[1] > curY or tailPos[1] < nextY:

					# Cut down until we are in the closest zig/zag to the apple
					while (nextY + 1) < curY:
						# move 1 Zig and 1 Zag
						move(South)
						# Update the headPos
						curY -= 1
						headIdx = (headIdx + 1) % bufferLen
						bodyBuffer[headIdx] = (curX, curY)

						move(South)
						# Update the headPos
						curY -= 1
						headIdx = (headIdx + 1) % bufferLen
						bodyBuffer[headIdx] = (curX, curY)

			# If the apple is above us
			elif nextY > curY:
				
				tailIdx = (headIdx - bodyLen + 1) % bufferLen
				tailPos = bodyBuffer[tailIdx]

				# Check if the tail is to the north of us
				if tailPos[1] > curY:
					
					# Cut down to the bottom of the map
					while curY > 0:
						move(South)

						# Update the headPos
						curY -= 1
						
						headIdx = (headIdx + 1) % bufferLen
						bodyBuffer[headIdx] = (curX, curY)

					# Cut back to the starting point
					while curX > 0:
						move(West)
						# Update the headPos
						curX -= 1
						
						headIdx = (headIdx + 1) % bufferLen
						bodyBuffer[headIdx] = (curX, curY)

	# Phase 3: Brute Force Hamiltonian
	# For long snakes, just brute force the hamiltonian method
	# it takes longer to evaluate shortcuts otherwise
	ableToMove = True
	while ableToMove:
		# Get the direciton to move next
		dir = HamiltonianCoordToDirArr[curX][curY]

		# See if we are over the apple coordinates
		if curX == nextX and curY == nextY :
			# Get next apple coords - check for end game condition
			appleCoord = measure()
			if appleCoord == None:
				break
			nextX, nextY = appleCoord
			# Body will grow on move
			bodyLen += 1

		# Move in the next Direciton
		ableToMove = move(dir)

		# Update the headPos
		dx, dy = DIRECTION_OFFSET[dir]
		curX += dx
		curY += dy

	# Equip Default hat- Harvests Tail
	change_hat(Hats.Straw_Hat)

# Pre-Calculated Hamiltonion
def CalcHamiltonionPath(_dim):
	visited = []
	nextDir = []
	CoordToIndex = {}
	IndexToCoord = {}
	CoordToIndexArray = []
	for x in range(_dim):
		CoordToIndexArray.append([])
		for y in range(_dim):
			CoordToIndexArray[x].append([])

	path = {}

	bodyBuffer = []
	bufferLen = len(HamiltonianPath)
	for i in range(bufferLen):
		bodyBuffer.append((-1,-1))

	resetPos()

	visited.append((get_pos_x(), get_pos_y()))
	# Generate Looping path without edge rollover
	# Move to top left corner
	for i in range(_dim - 1):
		path[(get_pos_x(), get_pos_y())] = North
		CoordToIndexArray[get_pos_x()][get_pos_y()] = North
		nextDir.append(North)
		moveForward()
		visited.append((get_pos_x(), get_pos_y()))

	# move to top right corner
	for i in range(_dim - 1):
		path[(get_pos_x(), get_pos_y())] = East
		CoordToIndexArray[get_pos_x()][get_pos_y()] = East
		nextDir.append(East)
		moveRight()
		visited.append((get_pos_x(), get_pos_y()))

	# Move down one
	path[(get_pos_x(), get_pos_y())] = South
	CoordToIndexArray[get_pos_x()][get_pos_y()] = South
	nextDir.append(South)
	moveBackwards(1, False)
	visited.append((get_pos_x(), get_pos_y()))

	# ZigZag back down to the first row
	for i in range((_dim // 2) - 1):
		# Left to before the first column
		for i in range(_dim - 2):
			path[(get_pos_x(), get_pos_y())] = West
			CoordToIndexArray[get_pos_x()][get_pos_y()] = West
			nextDir.append(West)
			moveLeft()
			visited.append((get_pos_x(), get_pos_y()))

		# Move down one
		path[(get_pos_x(), get_pos_y())] = South
		CoordToIndexArray[get_pos_x()][get_pos_y()] = South
		nextDir.append(South)
		moveBackwards(1, False)
		visited.append((get_pos_x(), get_pos_y()))
		
		# Right to the edge
		for i in range(_dim - 2):
			path[(get_pos_x(), get_pos_y())] = East
			CoordToIndexArray[get_pos_x()][get_pos_y()] = East
			nextDir.append(East)
			moveRight()
			visited.append((get_pos_x(), get_pos_y()))
		
		# Move down one
		path[(get_pos_x(), get_pos_y())] = South
		CoordToIndexArray[get_pos_x()][get_pos_y()] = South
		nextDir.append(South)
		moveBackwards(1, False)
		visited.append((get_pos_x(), get_pos_y()))

	# Left to before the first column
	for i in range(_dim - 1):
		path[(get_pos_x(), get_pos_y())] = West
		CoordToIndexArray[get_pos_x()][get_pos_y()] = West
		nextDir.append(West)
		moveLeft()
		visited.append((get_pos_x(), get_pos_y()))

	nextDir.append(West)

	count = 0
	for coord in path:
		CoordToIndex[coord] = count
		IndexToCoord[count] = coord
		count += 1

	print(len(visited))
	print(visited)
	print(len(nextDir))
	print(nextDir)
	print(len(CoordToIndex))
	print(CoordToIndex)
	print(len(IndexToCoord))
	print(IndexToCoord)
	print(len(path))
	print(path)
	print(len(CoordToIndexArray))
	print(CoordToIndexArray)
	print(len(bodyBuffer))
	print(bodyBuffer)

def testHamiltonianPath():
	for dir in HamiltonianDirs:
		move(dir)

	for coord in HamiltonianPath:
		moveTo(coord)

def dinosaurWorker(conditionFcn):
	#worldSize = get_world_size()

	#set_world_size(worldSize)

	#_dim = worldSize
	# Zero Based Dimension
	#zDim = _dim - 1

	while conditionFcn():
		playSnake()

# Test what farm size has the best Bone/Time ratio
#4 : 2162.94
#6 : 3003.17
#8 : 4171.38
#10 : 4849.67
#12 : 6290.72
#14 : 7557.88
#16 : 8873.57
#18 : 10547.73
#20 : 12087.99
#22 : 12939.96
#24 : 14535.56
#26 : 14961.28
#28 : 16073.31
#30 : 17122.07
#32 : 17918.49 !!!!!!!!!
def dinoTest():
	# For every even-farm size from 4-32
	for i in range(4, 33, 2):
		set_world_size(i)

		_dim = i
		# Zero Based Dimension
		zDim = _dim - 1

		startBones = num_items(BONES)
		startTime = get_time()
		# Play 5 times to find an average
		for j in range(5):
			playSnake(zDim)

		endTime = get_time()
		endBones = num_items(BONES)

		bonePerTime = (endBones - startBones) / (endTime - startTime)
		print(i, ":", bonePerTime)
