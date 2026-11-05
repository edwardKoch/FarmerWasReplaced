from _move_ import *

# Constants
MAX_SUNFLOWER = 15
MIN_SUNFLOWER = 7

def waitForSunToGrow():
	# Wait until a space is grown
	while not can_harvest() and get_entity_type() != None:
		continue

def harvestAllOf(plot, value):
	# Harvest all sunflowers of a certain value in a plot
	# plot: List of Tuples for coordinates (x, y)
	# value: number from MIN to MAX sunflower value
	# RETURNS: plot list but without the spaces that were harvested

	remainingPlot = []
	for x, y in plot:
		moveTo((x,y))

		waitForSunToGrow()

		if measure() == value:
			anyHarvested = True
			harvest()
		else:
			remainingPlot.append((x,y))

	return remainingPlot


def processSunflowerPlot(plot):
	# Process Sunflower Plot until harvested
	# plot: List of Tuples for coordinates (x, y)

	remainingPlot = []

	# Plant first round of Sunflowers
	for x, y in plot:
		moveTo((x,y))
		remainingPlot.append((x,y))
		if get_entity_type() != Entities.Sunflower:
			plant(Entities.Sunflower)

	# Harvest a plot of sunflowers in descending order
	for val in range(MAX_SUNFLOWER, MIN_SUNFLOWER - 1, -1):
			remainingPlot = harvestAllOf(remainingPlot, val)