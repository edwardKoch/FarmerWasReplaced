from _move_ import *
from _plant_ import *
from _farm_ import *
from _pumpkins_ import *
from _sunflowers_ import *
from _polycultre_ import *
from _cactus_ import *
from _maze_ import *
from _unlocks_ import *

resetFarm()

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
	checkAndUnlock(Unlocks.Leaderboard)

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

	worker = spawn_drone(processPumpkinPlot, PLOTS[Entities.Pumpkin])
	if worker != None:
		workers.append(worker)
	# If no workers available, process with main drone
	else:
		processPumpkinPlot(PLOTS[Entities.Pumpkin])

	# Do Polyculture with the 'main' drone to buy time
	processPolyPlot(PLOTS[Entities.Grass])

	# Wait for all workers to be done - aggregate results
	for minion in workers:
		wait_for(minion)

	# Run 4 Mazes
	workers = []
	numMaze = 4
	worker = spawn_drone(createAndSolveMazes, 0, 0, dim // 2, numMaze)
	if worker != None:
		workers.append(worker)
	# If no workers available, process with main drone
	else:
		createAndSolveMazes(0, 0, dim // 2, numMaze)

	worker = spawn_drone(createAndSolveMazes, 0, dim - 1, dim // 2, numMaze)
	if worker != None:
		workers.append(worker)
	# If no workers available, process with main drone
	else:
		createAndSolveMazes(0, dim - 1, dim // 2, numMaze)

	worker = spawn_drone(createAndSolveMazes, dim - 1, 0, dim // 2, numMaze)
	if worker != None:
		workers.append(worker)
	# If no workers available, process with main drone
	else:
		createAndSolveMazes(dim - 1, 0, dim // 2, numMaze)

	worker = spawn_drone(createAndSolveMazes, dim - 1, dim - 1, dim // 2, numMaze)
	if worker != None:
		workers.append(worker)
	# If no workers available, process with main drone
	else:
		createAndSolveMazes(dim - 1, dim - 1, dim // 2, numMaze)

	for minion in workers:
		wait_for(minion)
	
	# Run 1 Giant Dino
	# TODO - Dino
	resetFarm()