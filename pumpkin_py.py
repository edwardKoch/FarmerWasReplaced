from motion_py import *
from farming_py import *
from harvest_py import *
from plant_py import *

# Finds, Removes, and replants dead pumpkins in a line
# Line: list of coordinates
# Returns: True if there was a dead pumpkin in the line
def findAndReplaceDeadPumpInLine(line):
	wasDead = False
	for coord in line:

		# Go to assigned square
		moveTo(coord)

		# Wait for the pumpkin to grow
		# Doesnt die until fully grown
		waitForHarvest()	

		if get_entity_type() == DEAD_PUMP:
			wasDead = True
			# Replant - No Fertilizer, No Water, No Waiting, No Force
			harvestAndPlant(PUMPKIN, False, False, False, False)
			use_item(WATER)

	return wasDead

# Finds, removes, and replants dead pumpkins in all lines
# Lines: Dict of x/y value : Line 
# Returns: Dict of x/y value : True/False if there were dead pumpkins
def findAndReplaceDeadPumps(lines):
	deadPumps = {}
	
	def spawn(line):
		return spawn_drone(findAndReplaceDeadPumpInLine, line)

	def process(line):
		return findAndReplaceDeadPumpInLine(line)

	# For each line in lines, 
	deadPumps = processPerLine(lines, spawn, process)
						
	return deadPumps

def pumpkinWorker(conditionFcn):
	# Initialize entire plot to be "Dead Pumps"
	deadPumps = {}
	for xy in ROWS[PUMPKIN]:
		deadPumps[xy] = True
	
	# Initial Plant of Pumpkins - No Fertilizer, No Water, No Waiting, Force harvest
	harvestAndPlantAllEntity(PUMPKIN, False, False, False, True)

	# Forever
	while conditionFcn():
		# Populate Dead Pump Lines based on T/F map
		# Count how many rows contain dead pumps
		count = 0
		# Track rows that still contain dead pumpkins
		deadPumpLines = {}
		for xy in deadPumps:
			if deadPumps[xy]:
				count += 1
				deadPumpLines[xy] = ROWS[PUMPKIN][xy]

		# If all pumpkins are alive, just harvest them all
		# Assume search for deads leaves us on a pumpkin square
		if count == 0:
			# A single harvest will harvest all pumpkins
			harvest()
			# Go through and plant all Pumpkins
			# No Fertilizer, Water
			plantAllEntity(PUMPKIN, False, True)
			# Reset the search to the entire plot
			for xy in ROWS[PUMPKIN]:
				deadPumps[xy] = True
		else:
		# Find and Replace all Dead Pumpkins
			# Will return the sub-set of the plot that was dead
			# So next loop will only check the previously dead ones
			deadPumps = findAndReplaceDeadPumps(deadPumpLines)