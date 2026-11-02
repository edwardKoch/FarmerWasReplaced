from _move_ import *
from _plant_ import *
from _farm_ import *
from _unlocks_ import *

resetFarm()

####################
# Phase 1
# Unlock Trees, Pumpkins, and Sunflowers
# Uses linear farming only
####################

entities = [Entities.Bush, Entities.Grass, Entities.Carrot]


# Goal for Phase 1 is to unlock Carrots, Trees, Pumpkins, and Sunflowers
unlocked = 0
while num_unlocked(Unlocks.Sunflowers) == 0 or num_unlocked(Unlocks.Pumpkins) == 0 or num_unlocked(Unlocks.Trees) == 0:
	
	# Unlock Speed & Expand along the way
	checkAndUnlock(Unlocks.Speed)
	checkAndUnlock(Unlocks.Expand)

	# Unlock Trees when we can
	checkAndUnlock(Unlocks.Trees)

	# Unlock Pumpkins when we can
	checkAndUnlock(Unlocks.Pumpkins)

	# Unlock Sunflowers when we can
	checkAndUnlock(Unlocks.Watering)
	checkAndUnlock(Unlocks.Sunflowers)

	for x in range(get_world_size()):
		for y in range(get_world_size()):

			if can_harvest():
				harvest()
			toPlant = entities[x % len(entities)]
			if toPlant == Entities.Bush:
				if num_unlocked(Unlocks.Trees) > 0 and y % 2 == 0:
					toPlant = Entities.Tree
			plant_(toPlant)
			
			move(North)
		move(East)
