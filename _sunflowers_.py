from _move_ import *
from _algo_ import *
from _plant_ import *

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

def processSunflowerPlotMulti(plot):
	# Process Sunflower Plot until harvested - use multiple drones
	# plot: List of Tuples for coordinates (x, y)

	remainingPlot = []

	# Plant first round of Sunflowers
	plantPlotMulti_(Entities.Sunflower, plot)

	# Split plot into Rows & cols
	Rows, Cols = plotToRowsCols(plot)

	# Wait for the first flower to be done growing
	# Avoids wasting drones
	moveTo(plot[0])
	waitForSunToGrow()
			
	# Harvest a plot of sunflowers in descending order
	for val in range(MAX_SUNFLOWER, MIN_SUNFLOWER - 1, -1):
		# Define Process Functions based on value
		def spawn(line):
			return spawn_drone(harvestAllOf, line, val)

		def process(line):
			return harvestAllOf(line, val)
		
		remainingInRow = processPerLine(Rows, spawn, process)
		remaining = []
		for xy in remainingInRow:
			remaining += remainingInRow[xy]

		Rows, Cols = plotToRowsCols(remaining)
