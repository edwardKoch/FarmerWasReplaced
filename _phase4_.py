from _move_ import *
from _plant_ import *
from _farm_ import *
from _pumpkins_ import *
from _sunflowers_ import *
from _polycultre_ import *
from _cactus_ import *
from _maze_ import *
from _dinos_ import *
from _unlocks_ import *

resetFarmMulti()

####################
# Phase 4
# Unlock Leaderboard
# Plot based planting with Mazes then Dinos until unlock
####################

# Grass == Polyculture, Bush = Maze
# Put Maze first so that it can be started at 0,0
entities = [Entities.Bush, Entities.Grass, Entities.Pumpkin, Entities.Sunflower]

WholeFarm = []
dim = get_world_size()
for x in range(dim):
	for y in range(dim):
		WholeFarm.append((x, y))

PLOTS = assignEntitiesToQuads(entities)

# Track how many bones we will need
bonesNeeded = get_cost(Unlocks.Leaderboard)[Items.Bone]

while num_unlocked(Unlocks.Leaderboard) == 0:
	# Unlock Speed & Expand along the way
	checkAndUnlock(Unlocks.Speed)
	if checkAndUnlock(Unlocks.Expand):
		PLOTS = assignEntitiesToQuads(entities)
		WholeFarm = []
		dim = get_world_size()
		for x in range(dim):
			for y in range(dim):
				WholeFarm.append((x, y))


	# Unlock Resources along the way
	checkAndUnlock(Unlocks.Watering)
	checkAndUnlock(Unlocks.Fertilizer)

	# Unlock Yield along the way
	checkAndUnlock(Unlocks.Grass)
	checkAndUnlock(Unlocks.Carrots)
	checkAndUnlock(Unlocks.Trees)
	checkAndUnlock(Unlocks.Pumpkins)
	checkAndUnlock(Unlocks.Cactus)
	checkAndUnlock(Unlocks.Polyculture)
	checkAndUnlock(Unlocks.Mazes)
	checkAndUnlock(Unlocks.Megafarm)
	checkAndUnlock(Unlocks.Dinosaurs)

	# Unlock Leaderboard when we can
	if not checkAndUnlock(Unlocks.Leaderboard):
		
		# Run a round of "Normal Farming"
		workers = []

		worker = spawn_drone(processCactiPlotMulti, PLOTS[Entities.Bush])
		if worker != None:
			workers.append(worker)
		# If no workers available, process with main drone
		else:
			processCactiPlotMulti(PLOTS[Entities.Bush])

		worker = spawn_drone(processSunflowerPlotMulti, PLOTS[Entities.Sunflower])
		if worker != None:
			workers.append(worker)
		# If no workers available, process with main drone
		else:
			processSunflowerPlotMulti(PLOTS[Entities.Sunflower])

		worker = spawn_drone(processPumpkinPlotMulti, PLOTS[Entities.Pumpkin])
		if worker != None:
			workers.append(worker)
		# If no workers available, process with main drone
		else:
			processPumpkinPlotMulti(PLOTS[Entities.Pumpkin])

		# Do Polyculture with the 'main' drone to buy time
		processPolyPlot(PLOTS[Entities.Grass])

		# Wait for all workers to be done - aggregate results
		for minion in workers:
			wait_for(minion)

		# Run 4 Mazes
		workers = []
		numMaze = max_drones()
		mazeSize = dim // 2

		# Move to the middle spot so that the
		# minions dont get in eachothers way
		moveTo((mazeSize, mazeSize))

		worker = spawn_drone(createAndSolveMazesMulti, 0, 0, mazeSize, numMaze)
		if worker != None:
			workers.append(worker)
		# If no workers available, process with main drone
		else:
			createAndSolveMazesMulti(0, 0, mazeSize, numMaze)

		worker = spawn_drone(createAndSolveMazesMulti, 0, dim - 1, mazeSize, numMaze)
		if worker != None:
			workers.append(worker)
		# If no workers available, process with main drone
		else:
			createAndSolveMazesMulti(0, dim - 1, mazeSize, numMaze)

		worker = spawn_drone(createAndSolveMazesMulti, dim - 1, 0, mazeSize, numMaze)
		if worker != None:
			workers.append(worker)
		# If no workers available, process with main drone
		else:
			createAndSolveMazesMulti(dim - 1, 0, mazeSize, numMaze)

		# Do the last maze with the 'main' drone to maximize usage
		createAndSolveMazesMulti(dim - 1, dim - 1, mazeSize, numMaze)

		for minion in workers:
			wait_for(minion)
		
		# Run 1 Giant Dino - if needed for unlock, because it takes forever to run
		if num_items(Items.Bone) < bonesNeeded:
			dynamicHamiltonSnake()
		
		# Till the whole farm to prepare for the next cycle
		resetFarmMulti()