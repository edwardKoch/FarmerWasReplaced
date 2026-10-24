from algorithms_py import *
from motion_py import *
from farming_py import *
from harvest_py import *
from plant_py import *

# Plants and returns a set of petal counts in a line
# Line: list of coordinates
# Returns: Set of counts that appear in the line
def plantAndMeasureLine(line):
	lineContainsCount = set()

	# For each space in the line
	for coord in line:
		moveTo(coord)
		# Plant a sunflower, no Fertilizer, no water
		plantEntity(SUNFLOWER, False, False)
		# Track the number of petals
		lineContainsCount.add(measure())

	return lineContainsCount

# Plants Sunflowers and Gets a dict of x/y value : counts
# Lines: Dict of x/y value : Line 
# Returns: Dict of x/y value : Set of counts that appear in the line
def plantAndMeasure(lines):
	# Sunflower Line Counts
	counts = {}

	def spawn(line):
		return spawn_drone(plantAndMeasureLine, line)

	def process(line):
		return plantAndMeasureLine(line)

	# For each line in lines, 
	counts = processPerLine(lines, spawn, process)

	return counts

# Harvest all the sunflowers in a line with a specific value
# Lines: Dict of x/y value : Line 
# Value: Number of petals to harvest
def harvestSunflowerLine(line, value):
	for coord in line:
		moveTo(coord)
		if measure() == value:
			# Harvest sunflower, wait for harvest
			harvestEntity(True, False)


# Harvest lines of sunflowers in decending petal count order
# Lines: Dict of x/y value : Line 
# Counts: Dict of x/y value : counts that appear in the line
def harvestSunflowerLines(lines, counts):
	# For each possible sunflower value
	for cnt in range(MAX_SUNFLOWER_PETALS, MIN_SUNFLOWER_PETALS-1, -1):
		# Track which lines should be harvested in this pass
		linesToHarvest = {}

		# For each x/y value of sunflowers
		for xy in lines:
			# If that line contains the current count to harvest
			if cnt in counts[xy]:
				linesToHarvest[xy] = lines[xy]

		def spawn(line):
			return spawn_drone(harvestSunflowerLine, line, cnt)

		def process(line):
			return harvestSunflowerLine(line, cnt)

		processPerLine(linesToHarvest, spawn, process)


def sunflowerWorker(conditionFcn):
	while conditionFcn():
		# Plant the next gen of sunflowers
		# and Get the Rows that contain the Sunflower counts
		PetalLocations = plantAndMeasure(ROWS[SUNFLOWER])

		# Wait for Sunflowers to finish growing
		# Assume most of plot is done growing because it takes
		# So long to plant the plot
		sSleep(2)

		# Harvest the Sunflowers in Order
		harvestSunflowerLines(ROWS[SUNFLOWER], PetalLocations)
