from farmTypes_py import *
from motion_py import *
from farm_py import *

from harvest_py import *
from plant_py import *

# Process an entity type
# Will Harvest if ready, then re-plant
# Fert: True if should fertilize
# Water: True if should use water
def processPlant(plot, entityType, fert, water):
	# Do not process non-basic plantable entitites
	#if entityType not in BASIC_ENTITIES:
	#	return
		
	# For all other types, harvest and plant all plots
	# Block harvest to ensure path efficiency, no force
	harvestAndPlantAllEntity(entityType, fert, water, True, False)
							
# Harvest, then plant an entity at current location
# EntityType: type to plant
# Fert: True if should fertilize
# Water: True if should use water
# Block: True if wait for harvest
# Force: True if harvest no matter what	
def harvestAndPlant(entityType, fert, water, block, force):		
	harvestEntity(block, force)
	plantEntity(entityType, fert, water)

# Harvest, then plant an entity in a plot
# Plot: list of coordinates
# EntityType: type to plant
# Fert: True if should fertilize
# Water: True if should use water
# Block: True if wait for harvest
# Force: True if harvest no matter what	
def harvestAndPlantPlot(plot, entityType, fert, water, block, force):		
	# Iterate through Plot for the entity
	for coord in plot:
		# Go to assigned square
		moveTo(coord)	
		# Harvest, Till, & Plant
		harvestAndPlant(entityType, fert, water, block, force)

# Harvest, then Plant all of an assigned entity type per ROW
# EntityType: Type to plant
# Fert: True if should use fertilizer
# Water: True if should use water
# Force: True if harvest no matter what	
def harvestAndPlantAllEntity(entityType, fert, water, block, force):
	
	def spawn(line):
		return spawn_drone(harvestAndPlantPlot, line, entityType, fert, water, block, force)

	def process(line):
		return harvestAndPlantPlot(line, entityType, fert, water, block, force)

	processPerLine(ROWS[entityType], spawn, process)
		
# Plot: list of squares to fertilize
def fertilizePlot(plot):
	# Iterate through Plot for the entity
	for coord in plot:
		# Go to assigned square
		moveTo(coord)
		if (num_items(FERTILIZER) > 0):
			use_item(FERTILIZER)	

# Plot: list of squares to water			
def waterPlot(plot):
	# Iterate through Plot for the entity
	for coord in plot:
		# Go to assigned square
		moveTo(coord)	
		while get_water() <= 0.75:
			use_item(WATER)