from _move_ import *

# Wait until a space is either grown or a dead pumpkin
def waitForPumpToGrow():
	while not can_harvest() and get_entity_type() != Entities.Dead_Pumpkin and get_entity_type() != None:
		continue

# Replace each dead pumpkin in a plot
def replaceDeadPumpkins(plot):
	# plot: List of Tuples for coordinates (x, y)

	anyDead = False
	for x, y in plot:
		moveTo((x,y))

		waitForPumpToGrow()

		if get_entity_type() == Entities.Dead_Pumpkin:
			anyDead = True
			harvest()
			plant(Entities.Pumpkin)

	return anyDead

# Process Pumpkin Plot until harvested
def processPumpkinPlot(plot):
	# Plant first round of pumpkins
	for x, y in plot:
		moveTo((x,y))
		if get_entity_type() != Entities.Pumpkin:
			plant(Entities.Pumpkin)

	# Recursiveley replace pumpkins
	while replaceDeadPumpkins(plot):
		continue

	# harvest the giant pumpkin
	harvest()