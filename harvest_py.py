from farmTypes_py import *
from algorithms_py import *
from motion_py import *

from farm_py import *

# Wait until a plant is ready for harvest
def waitForHarvest():
	while not can_harvest() and get_entity_type() in HARVESTABLE_ENTITIES:
		continue

# Block: True if this should be a blocking call
# False if it should skip over
# Force: True if this should be harvested no matter what
# False otherwise
def harvestEntity(block, force):
	if block:
		waitForHarvest()
		harvest()
	# Check if plant is available for harvest
	elif can_harvest():
		harvest()
	elif force:
		harvest()

# Harvest a plot
# Plot: list of coordinates
# Block: True if this should be a blocking call
# False if it should skip over
# Force: True if this should be harvested no matter what
# False otherwise
def harvestPlot(plot, block, force):
	# Iterate through Plot
	for coord in plot:
		# Go to assigned square
		moveTo(coord)	
		harvestEntity(block, force)

		
# Harvest all of an assigned entity type per ROW
# EntityType: type to plant
# Block: True if this should be a blocking call
# False if it should skip over
# Force: True if this should be harvested no matter what
# False otherwise
def harvestAllEntity(entityType, block, force):

	def spawn(line):
		return spawn_drone(harvestPlot, line, block, force)

	def process(line):
		return harvestPlot(line, block, force)

	processPerLine(ROWS[entityType], spawn, process)