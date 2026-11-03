from _move_ import *
from _plant_ import *
from _farm_ import *
from _pumpkins_ import *
from _sunflowers_ import *
from _polycultre_ import *
from _unlocks_ import *

resetFarm()

####################
# Phase 3
# Unlock Multi-Drones
# Plot based planting with Mazes & Polyculture
####################

# Grass == Polyculture, Bush = Maze
entities = [ Entities.Grass, Entities.Bush, Entities.Pumpkin, Entities.Sunflower]

PLOTS = assignEntitiesToQuads(entities)

# TEMP:
entities = [Entities.Bush, Entities.Grass, Entities.Carrot, Entities.Pumpkin]
PLOTS = assignEntitiesToQuads(entities)
while True:
	# Unlock Speed & Expand along the way
	checkAndUnlock(Unlocks.Speed)
	if checkAndUnlock(Unlocks.Expand):
		PLOTS = assignEntitiesToQuads(entities)

	# Unlock Yield along the way
	checkAndUnlock(Unlocks.Watering)
	checkAndUnlock(Unlocks.Grass)
	checkAndUnlock(Unlocks.Carrots)
	checkAndUnlock(Unlocks.Trees)
	checkAndUnlock(Unlocks.Pumpkins)

	# Unlock Polyculture when we can
	checkAndUnlock(Unlocks.Polyculture)

	# Unlock Cacti when we can
	checkAndUnlock(Unlocks.Cactus)

	for toPlant in PLOTS:
		if toPlant == Entities.Pumpkin:
			processPumpkinPlot(PLOTS[toPlant])
		elif toPlant == Entities.Grass:
			processPolyPlot(PLOTS[toPlant])
		else:
			plantPlot_(toPlant, PLOTS[toPlant])