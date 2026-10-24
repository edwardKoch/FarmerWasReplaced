from farm_py import *
from farming_py import *
from workers_py import *

clear()
resetPos()
initFarm()

# Track what entities the minions are planting
PLANT_MINIONS = []

# Track what entities the minions are watering
WATER_MINIONS = []

# Have workers run forever
def condition():
	return True

# Spawn drones to handle all plantable entities
for entity in PLANTABLE_ENTITIES:
	if entity != GRASS and len(ASSIGNMENTS[entity]) > 0:
		if spawn_drone(farmWorker, entity, condition):
			PLANT_MINIONS.append(entity)

# Spawn 9 PolyCulture Drones
width = 5
cent = width // 2
for x in range(cent, 15, width):
	for y in range(cent, 15, width):
		if spawn_drone(polyWorker, condition, x, y, width) == None:
			polyWorker(x, y, width)

# Spawn Water Minions
for entity in WATERABLE_ENTITIES:
	if spawn_drone(waterWorker, entity, condition):
		WATER_MINIONS.append(entity)

# Use main drone to track resource count & do mazes
LAST_COUNT = {}
for item in COUNTABLE_ITEMS:
	LAST_COUNT[item] = num_items(item)

# Do 10 Mazes, then check items
while condition():
	if MAZE_ENABLE:
		for i in range (10):
			createAndSolveMaze(MAZE_X, MAZE_Y, MAZE_DIM)

	for item in COUNTABLE_ITEMS:
		num = num_items(item)
		if num < LAST_COUNT[item]:
			print("OH NO:", item)
		LAST_COUNT[item] = num
	
# Use main drone just do mazes
# Will use available drone pool for maze accelaration
#if MAZE_ENABLE:
	#mazeWorker()
