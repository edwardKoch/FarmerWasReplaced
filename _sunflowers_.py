from _move_ import *

# Constants
MAX_SUNFLOWER = 15
MIN_SUNFLOWER = 7

# Wait until a space is grown
def waitForSunToGrow():
	while not can_harvest():
		continue

# Harvest all sunflowers of a certain value in a plot
def harvestAllOf(plot, value):
    # plot: List of Tuples for coordinates (x, y)
    # value: number from MIN to MAX sunflower value

	anyHarvested = False
	for x, y in plot:
		moveTo((x,y))

		waitForSunToGrow()

		if measure() == value:
			anyHarvested = True
			harvest()

	return anyHarvested

# Harvest a plot of sunflowers in descending order
def harvestInOrder(plot):
	for val in range(MAX_SUNFLOWER, MIN_SUNFLOWER - 1, -1):
		harvestAllOf(plot, val)