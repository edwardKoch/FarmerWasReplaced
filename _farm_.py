from _move_ import *
from _algo_ import *

def resetFarm():
	moveTo((0,0))
	clear()

	# Till the entire Farm - everything grows on soil
	for x in range(get_world_size()):
		for y in range(get_world_size()):

			harvest()
			if get_ground_type() != Grounds.Soil:
				till()
		
			move(North)
		move(East)

def resetFarmMulti():
	# Till the entire Farm - everything grows on soil

	WholeFarm = []
	dim = get_world_size()
	for x in range(dim):
		for y in range(dim):
			WholeFarm.append((x, y))

	# Split plot into Rows & cols
	Rows, Cols = plotToRowsCols(WholeFarm)

	def resetFarmCol(plot):
		for x, y in plot:
			moveTo((x,y))
			harvest()
			if get_ground_type() != Grounds.Soil:
				till()

	def spawn(line):
		return spawn_drone(resetFarmCol, line)

	def process(line):
		return resetFarmCol(line)

	clear()

	# Till the entire Farm - everything grows on soil
	processPerLine(Rows, spawn, process)

def assignEntitiesToQuads(entities):
	# Assigns a list of coordinates to each of 4 entities
	# entities: list of Entities to assign, max len = 4
	# RETURN: dictionary of {Entity:[(x, y)...]}
	
	plots = {}
	
	for ent in entities:
		plots[ent] = []

	dim = get_world_size()
	half = dim // 2
	for x in range(dim):
		for y in range(dim):

			# Calculate the quadrant
			if x < half:
				if y < half:
					quad = 0
				else:
					quad = 1

			elif y >= half:
				quad = 3
			else:
				quad = 2

			toPlant = entities[quad % len(entities)]
			plots[toPlant].append((x,y))

	return plots