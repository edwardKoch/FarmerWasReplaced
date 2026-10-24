from farmTypes_py import *
from areas_py import *
from algorithms_py import *

DIM = get_world_size()

# Holds a 2-D [x][y] array of Entities
FARM = []

# Holds a 1D list of Farm Coordinates (x, y)
WHOLE_FARM = []

# Holds (x, y) pairs for all assignments for each entity type
PLOTS = {}

# Holds a Dictionary of Rows for each entity type
# Where Rows is a dict of y coord to a row
# and a row is a list of squares with the same y coord
# sorted by x value
# Even Ys will be sorted x -> X
# Odd Ys will be sorted X -> x
# To aid in zig-zag processing
ROWS = {}

# Holds a Dictionary of Cols for each entity type
# Where Cols is a dict of x coord to a col
# and a col is a list of squares with the same x coord
# sorted by y value
# Even Xs will be sorted y -> Y
# Odd Xs will be sorted Y -> y
# To aid in zig-zag processing
COLS = {}

# Assign Entities to AREAS
# Actual Assignments
ASSIGNMENTS = {
	CACTUS    : [ESE],
	CARROT    : [],
	GRASS     : [SW],
	PUMPKIN   : [NW],
	SUNFLOWER : [SSE, SE_DIAG],
	TREE      : [],
	HEDGE     : [NE] # Assign maze to NE to get out of the way
	}
# Test Assignments
#ASSIGNMENTS = {
#	CACTUS    : [NW_DIAG, WSW, ENE],
#	CARROT    : [SE_DIAG, SSW, NNE],
#	GRASS     : [],
#	PUMPKIN   : [SW_DIAG, NNW, SSE],
#	SUNFLOWER : [NE_DIAG, WNW, ESE],
#	TREE      : [],
#	HEDGE     : []
#	}
# Track the last time that all entities were planted
LAST_PLANTED = {}

# If we should dedicate spaces for Mazes
MAZE_ENABLE = True
# Assign the last nxn
# Use all but m of the NE quadrant
MAZE_OFFSET = 0
MAZE_DIM = (DIM // 2) - MAZE_OFFSET
MAZE_X = DIM - 1
MAZE_Y = DIM - 1

def initFarm():
	global FARM
	global LAST_PLANTED
	global PLOTS
		
	# Match actual farm to farm representation
	clear()
	for x in range(DIM):
		FARM.append([])
		for y in range(DIM):
			FARM[x].append(GRASS)
			WHOLE_FARM.append((x, y))
	
	# Clear last time planted
	for entity in ENTITIES:
		LAST_PLANTED[entity] = 0
	
	# Initialize Plot Assignments
	for entity in ENTITIES:
		PLOTS[entity] = []	
	
	# Assign Entities to their plots
	for entity in PLANTABLE_ENTITIES:
		assignEntity(entity)
	
	# Overwrite first space of Hedges with bush for Maze
	if MAZE_ENABLE:
		assignMaze()

	# Because GRASS is the 'Default' and may not be explicitly
	# assigned a plot, make sure all Grass spots are assigned
	assignGrass()

	# Calculate all the Rows and Cols of a given entity
	for entity in ENTITIES:
		calculateRowsCols(entity)	
	
# Assign Pumpkins to the Correct Quadrant
def assignEntity(entity):
	global FARM
	global PLOTS
	
	# Iterate through entire FARM
	for area in ASSIGNMENTS[entity]:
		for x,y in AREAS[area]:
			FARM[x][y] = entity
			PLOTS[entity].append((x, y))

def assignMaze():
	# Start in the NE Corner
	start = DIM - 1
	for x in range(start, start-MAZE_DIM, -1):
		for y in range(start, start-MAZE_DIM, -1):
			FARM[x][y] = HEDGE
			PLOTS[HEDGE].append((x, y))
	FARM[MAZE_X][MAZE_Y] = BUSH
	PLOTS[BUSH].append((MAZE_X, MAZE_Y))

def assignGrass():
	PLOTS[GRASS] = []
	for x in range(DIM):
		for y in range(DIM):
			if FARM[x][y] == GRASS:
				PLOTS[GRASS].append((x, y))

def calculateRowsCols(entityType):
	ROWS[entityType] = {}
	COLS[entityType] = {}

	# Create References to ROWS/COLS
	Rows = ROWS[entityType]
	Cols = COLS[entityType]

	# Init the Rows/Cols
	for i in range(DIM):
		Rows[i] = []
		Cols[i] = []

	# Get the assigned plot
	plot = PLOTS[entityType]

	for square in plot:
		Rows[square[1]].append(square)
		Cols[square[0]].append(square)

		# Sort all Rows & Cols
	for i in range(DIM):
		# Sort all Rows & Cols, using p1 > p2
		bubbleSort(Rows[i], dirCompare(0, True))
		bubbleSort(Cols[i], dirCompare(1, True))
		
	# Remove empty lists
	for i in range(DIM):
		if len(Rows[i]) < 1:
			Rows.pop(i)
		if len(Cols[i]) < 1:
			Cols.pop(i)