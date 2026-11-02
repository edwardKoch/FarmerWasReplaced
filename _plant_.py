from _move_ import *

def plant_(entity):
	# Tills if necessary & Plants an entity
	# entity: entity to plant from Entites.*

	if entity == Entities.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()

	plant(entity)

def plantTreeBush_(x, y):
	# Plants a checkerboard pattern of trees and bushes
	# x, y: coordinates to plant

	toPlant = Entities.Bush
	if y % 2 == 0 and x % 2 == 0:
		toPlant = Entities.Tree
	elif y % 2 == 1 and x % 2 == 1:
		toPlant = Entities.Tree

	plant_(toPlant)

def plantPlot_(entity, plot):
	# Plants an entity in a plot
	# entity: entity to plant from Entites.*
	# plot: list of (x, y) coordinates to plant

	for x, y in plot:

		moveTo((x, y))

		if can_harvest():
			harvest()
			
		if entity == Entities.Bush:
			plantTreeBush_(x, y)
		else:
			plant_(entity)