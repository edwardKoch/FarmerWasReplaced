from _move_ import *
from _plant_ import *
from _pumpkins_ import *

moveTo((0,0))

####################
# Phase 2
# Unlock Polyculture & Cacti
# Uses quadrant farming for Pumpkin Maxing, ignore sunflowers until Polyculture
####################

entities = [Entities.Bush, Entities.Grass, Entities.Carrot, Entities.Pumpkin]

# Till the entire Farm - everything grows on soil
for x in range(get_world_size()):
	for y in range(get_world_size()):

		if get_ground_type() != Grounds.Soil:
			till()
		
		move(North)
	move(East)


# Assign entities to a plot of land
entities = [Entities.Bush, Entities.Grass, Entities.Carrot, Entities.Pumpkin]
# TODO replace with dictionary
PLOTS = []

# Add a list of coordinates for each entity
def assignEntities():
	for ent in entities:
		PLOTS.append([])

	dim = get_world_size()
	half = dim // 2
	for x in range(dim):
		for y in range(dim):

			# Calculate the quadrant
			if x < half:
				if y < half:
					quad = 0
				else:
					quad = 1

			elif y >= half:
				quad = 3
			else:
				quad = 2
			if can_harvest():
				harvest()

			PLOTS[quad].append((x,y))

assignEntities()

# Goal for Phase 2 is to unlock Polyculture & Cacti
unlocked = 0
while num_unlocked(Unlocks.Polyculture) == 0 or num_unlocked(Unlocks.Cactus) == 0:
	# Unlock Speeds along the way
	if num_items(Items.Wood) > 20:
		# TODO Unlock Speed 2
		pass

	# Unlock FarmSize along the way
	if num_items(Items.Pumpkin) > 1000:
		# TODO Unlock Speed 2
		assignEntities()
		pass

    # Unlock Yield along the way
	# TODO Check Grass
	# TODO Check Carrots
	# TODO Check Trees

	# Unlock Polyculture when we can
	if num_items(Items.Pumpkin) > 3000:
		# TODO Unlock Polyculture
		unlocked += 1

	# Unlock Cacti when we can
	if num_items(Items.Pumpkin) > 5000:
		# TODO Unlock Cactus
		unlocked += 1

	dim = get_world_size()
	half = dim // 2
	for x in range(dim):
		for y in range(dim):

			moveTo((x, y))
			# Calculate the quadrant
			if x < half:
				if y < half:
					quad = 0
				else:
					quad = 1

			elif y >= half:
				quad = 3
			else:
				quad = 2
			if can_harvest():
				harvest()
				
			toPlant = entities[quad % len(entities)]
			if toPlant == Entities.Bush:
				plantTreeBush_(x, y)
			elif toPlant == Entities.Pumpkin:
				processPumpkinPlot(PLOTS[3])
				# Skip the rest of the column
				break
			else:
				plant_(toPlant)

