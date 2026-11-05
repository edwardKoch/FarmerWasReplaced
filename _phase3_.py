from _move_ import *
from _plant_ import *
from _farm_ import *
from _pumpkins_ import *
from _sunflowers_ import *
from _polycultre_ import *
from _maze_ import *
from _unlocks_ import *

resetFarm()

####################
# Phase 3
# Unlock Multi-Drones
# Plot based planting with Mazes & Polyculture
####################

# Grass == Polyculture, Bush = Maze
# Put Maze first so that it can be started at 0,0
entities = [Entities.Bush, Entities.Grass, Entities.Pumpkin, Entities.Sunflower]

PLOTS = assignEntitiesToQuads(entities)

while num_unlocked(Unlocks.Megafarm) == 0:
	# Unlock Speed & Expand along the way
	checkAndUnlock(Unlocks.Speed)
	if checkAndUnlock(Unlocks.Expand):
		PLOTS = assignEntitiesToQuads(entities)

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

	# Unlock Megafarms when we can
	checkAndUnlock(Unlocks.Megafarm)

	# Plant Pumpkins if needed
	if num_items(Items.Pumpkin) < 10000:
		processPumpkinPlot(PLOTS[Entities.Pumpkin])

	# Plant Sunflowers if needed
	if num_items(Items.Power) < 10000:
		processSunflowerPlot(PLOTS[Entities.Sunflower])

	# Run a Polyculture Plot
	processPolyPlot(PLOTS[Entities.Grass])

	# Run 4 Mazes
	for i in range(4):
		createAndSolveMaze(0, 0, get_world_size() // 2)
