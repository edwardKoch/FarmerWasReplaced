from farmTypes_py import *
from algorithms_py import *
from motion_py import *

from farm_py import *

# Plant an entity at the current location
# EntityType: type to plant
# Fert: True if should use fertilizer
# Water: True if should use water
def plantEntity(entityType, fert, water):
	global LAST_PLANTED
	
	# Till if needed
	if get_ground_type() != SOILS[entityType]:
		till()
		
	# Plant the entity
	if COSTS[entityType] == []:
		plant(entityType)
	else:
		for item, cost in COSTS[entityType]:
			if num_items(item) < cost:
				return
		plant(entityType)
	
	# Update Last Planted time for this entity type
	LAST_PLANTED[entityType] = get_time()
	
	# Fertilize if able
	if fert and (num_items(FERTILIZER) > 0):
		use_item(FERTILIZER)

	# Water if able
	if water and (num_items(WATER) > 0):
		use_item(WATER)

# Plant an entity in a plot
# Plot: list of coordinates
# EntityType: type to plant
# Fert: True if should use fertilizer
# Water: True if should use water
def plantPlot(plot, entityType, fert, water):
	# Iterate through Plot for the entity
	for coord in plot:
		# Go to assigned square
		moveTo(coord)	
		plantEntity(entityType, fert, water)

		
# Plant all of an assigned entity type per ROW
# EntityType: Type to plant
# Fert: True if should use fertilizer
# Water: True if should use water
def plantAllEntity(entityType, fert, water):

	def spawn(line):
		return spawn_drone(plantPlot, line, entityType, fert, water)

	def process(line):
		return plantPlot(line, entityType, fert, water)

	processPerLine(ROWS[entityType], spawn, process)