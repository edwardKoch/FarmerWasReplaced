from _move_ import *
from _plant_ import *

moveTo((0,0))

####################
# Phase 1
# Unlock Trees, Pumpkins, and Sunflowers
# Uses linear farming only
####################

entities = [Entities.Bush, Entities.Grass, Entities.Carrot]

# Till the entire Farm - everything grows on soil
for x in range(get_world_size()):
	for y in range(get_world_size()):

		if get_ground_type() != Grounds.Soil:
			till()
		
		move(North)
	move(East)

# Goal for Phase 1 is to unlock Carrots, Trees, Pumpkins, and Sunflowers
unlocked = 0
while num_unlocked(Unlocks.Sunflowers) == 0 or num_unlocked(Unlocks.Pumpkins) == 0 or num_unlocked(Unlocks.Trees) == 0:
	
	# Unlock Speeds along the way
	if num_items(Items.Wood) > 20:
		# TODO Unlock Speed 2
		pass

	# Unlock Trees when we can
	if num_items(Items.Carrot) > 70 and num_items(Items.Wood) > 50:
		# TODO Unlock Trees
		unlocked += 1

	# Unlock Pumpkins when we can
	if num_items(Items.Carrot) > 200 and num_items(Items.Wood) > 500:
		# TODO Unlock Pumpkins
		unlocked += 1

	# Unlock Sunflowers when we can
	if num_items(Items.Carrot) > 500 and num_items(Items.Wood) > 50:
		# TODO Unlock Water
		# TODO Unlock Sunflower
		unlocked += 1

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
