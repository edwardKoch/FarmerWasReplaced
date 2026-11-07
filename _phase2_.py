from _move_ import *
from _plant_ import *
from _farm_ import *
from _pumpkins_ import *
from _unlocks_ import *

resetFarm()

####################
# Phase 2
# Unlock Polyculture & Cacti & Mazes
# Uses quadrant farming for Pumpkin Maxing, ignore sunflowers until Polyculture
####################

# Assign entities to a plot of land
entities = [Entities.Bush, Entities.Grass, Entities.Carrot, Entities.Pumpkin]


PLOTS = assignEntitiesToQuads(entities)

# First Goal for Phase 2 is to unlock Polyculture & Cacti
unlocked = 0
while num_unlocked(Unlocks.Polyculture) == 0 or num_unlocked(Unlocks.Cactus) == 0:

	# Unlock Speed & Expand along the way
	checkAndUnlock(Unlocks.Speed)
	if checkAndUnlock(Unlocks.Expand):
		PLOTS = assignEntitiesToQuads(entities)
		resetFarm()

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

		else:
			plantPlot_(toPlant, PLOTS[toPlant])

# Second Goal for Phase 2 is to unlock Mazes - need Fertilizer first
while num_unlocked(Unlocks.Fertilizer) == 0:
	# Unlock Fertilizer when we can
	checkAndUnlock(Unlocks.Fertilizer)

	for toPlant in PLOTS:
		if toPlant == Entities.Pumpkin:
			processPumpkinPlot(PLOTS[toPlant])

		else:
			plantPlot_(toPlant, PLOTS[toPlant])

# Second Goal for Phase 2 is to unlock Mazes - use linear farming to manually fertilize
resetFarm()
while num_unlocked(Unlocks.Mazes) == 0:

	# Unlock Speed & Expand along the way
	checkAndUnlock(Unlocks.Speed)
	if checkAndUnlock(Unlocks.Expand):
		PLOTS = assignEntitiesToQuads(entities)

	# Unlock Yield along the way
	checkAndUnlock(Unlocks.Watering)
	checkAndUnlock(Unlocks.Fertilizer)
	checkAndUnlock(Unlocks.Grass)
	checkAndUnlock(Unlocks.Carrots)
	checkAndUnlock(Unlocks.Trees)
	checkAndUnlock(Unlocks.Pumpkins)

	# Unlock Mazes when we can
	checkAndUnlock(Unlocks.Mazes)

	# Use linear farming to control fertlizer
	for x in range(get_world_size()):
		for y in range(get_world_size()):

			if can_harvest():
				harvest()

			toPlant = entities[x % len(entities)]

			if toPlant == Entities.Bush:
				plantTreeBush_(x, y)
			else:
				plant_(toPlant)

			if num_items(Items.Fertilizer) > 0:
				use_item(Items.Fertilizer)
			
			move(North)
		move(East)