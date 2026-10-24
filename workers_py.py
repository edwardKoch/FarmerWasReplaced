from farmTypes_py import *
from farming_py import *
from farm_py import *
from path_py import *
from algorithms_py import *
from maze_py import *

from cactus_py import *
from dinosaur_py import *
from polyculture_py import *
from pumpkin_py import *
from sunflower_py import *

def waterWorker(entityType, conditionFcn):
	while conditionFcn():
		waterPlot(PLOTS[entityType])
		
# Repeatedly process a given entity
def farmWorker(entityType, conditionFcn):
	
	# Spawn specialty workers if needed
	if entityType == SUNFLOWER:
		return sunflowerWorker(conditionFcn)
	elif entityType == PUMPKIN:
		return pumpkinWorker(conditionFcn)
	elif entityType == CACTUS:
		return cactusWorker(conditionFcn)
		
	else:
		while conditionFcn():
			# Process the entity's plot, fertilize Trees
			processPlant(PLOTS[entityType], entityType, (entityType == TREE))

# Use the entire Farm for a single entity
# EntityType: Type to farm
# WorkerFcn: ther worker funciton to call for the entity
def megaWorker(entityType, workerFcn, conditionFcn):
	global ROWS
	global COLS
	global PLOTS

	ROWS[entityType] = {}
	COLS[entityType] = {}
	PLOTS = {}
	PLOTS[entityType] = []	

	# Store all the rows
	Rows = ROWS[entityType]

	# Store all the cols
	Cols = COLS[entityType]

	_dim = get_world_size()
	
	# Init the Rows/Cols
	for i in range(_dim):
		Rows[i] = []
		Cols[i] = []

	for x in range(_dim):
		for y in range(_dim):
			Rows[y].append((x, y))
			Cols[x].append((x, y))

		# Sort all Rows & Cols
	for i in range(_dim):
		# Sort all Rows & Cols, using p1 > p2
		bubbleSort(Rows[i], dirCompare(0, True))
		bubbleSort(Cols[i], dirCompare(1, True))
		
	# Remove empty lists
	for i in range(_dim):
		if len(Rows[i]) < 1:
			Rows.pop(i)
		else:
			PLOTS[entityType] += Rows[i]
		if len(Cols[i]) < 1:
			Cols.pop(i)


	farmWorker(entityType, conditionFcn)