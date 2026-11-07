from _move_ import *
from _algo_ import *
from _plant_ import *

def waitForPumpToGrow():
	# Wait until a space is either grown or a dead pumpkin
	while not can_harvest() and get_entity_type() != Entities.Dead_Pumpkin and get_entity_type() != None:
		continue

def replaceDeadPumpkins(deads):
	# Replace each dead pumpkin in a plot
	# deads: List of dead pumpkin coordinates (x, y)
	# RETURNS: list of dead pumpkin spots

	stillDead = []
	for x, y in deads:
		moveTo((x,y))

		waitForPumpToGrow()

		if get_entity_type() == Entities.Dead_Pumpkin:
			stillDead.append((x, y))
			harvest()
			plant(Entities.Pumpkin)

	return stillDead


def processPumpkinPlot(plot):
	# Process Pumpkin Plot until harvested
	# plot: List of Tuples for coordinates (x, y)

	deads = []
	# Plant first round of pumpkins
	for x, y in plot:
		moveTo((x,y))
		if get_entity_type() != Entities.Pumpkin:
			plant(Entities.Pumpkin)
			deads.append((x,y))


	# Recursiveley replace pumpkins

	deads = replaceDeadPumpkins(deads)
	while len(deads) != 0:
		deads = replaceDeadPumpkins(deads)

	# harvest the giant pumpkin
	harvest()

def processPumpkinPlotMulti(plot):
	# Process Pumpkin Plot until harvested - using multiple drones
	# plot: List of Tuples for coordinates (x, y)
	
	# Plant first round of Pumpkins
	plantPlotMulti_(Entities.Pumpkin, plot)

	deads = []
	for x, y in plot:
		deads.append((x,y))

	# Recursiveley replace pumpkins
	Rows, Cols = plotToRowsCols(deads)

	def spawn(line):
		return spawn_drone(replaceDeadPumpkins, line)

	def process(line):
		return replaceDeadPumpkins(line)

	while len(deads) != 0:
		deadResults = processPerLine(Rows, spawn, process)
		deads = []
		for xy in deadResults:
			deads += deadResults[xy]

		Rows, Cols = plotToRowsCols(deads)

	# harvest the giant pumpkin
	harvest()