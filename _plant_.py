from _move_ import *
from _algo_ import *

def plant_(entity):
	# entity: entity to plant from Entites.*

	plant(entity)

def plantTreeBush_(x, y):
	# Plants a checkerboard pattern of trees and bushes
	# x, y: coordinates to plant

	toPlant = Entities.Bush
	if y % 2 == 0 and x % 2 == 0:
		toPlant = Entities.Tree
	elif y % 2 == 1 and x % 2 == 1:
		toPlant = Entities.Tree

	plant(toPlant)

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
			plant(entity)

def plantPlotMulti_(entity, plot):
	# Plants an entity in a plot using multiple drones
	# entity: entity to plant from Entites.*
	# plot: list of (x, y) coordinates to plant

	# Split plot into Rows & cols
	Rows, Cols = plotToRowsCols(plot)
			
	def spawn(line):
		return spawn_drone(plantPlot_, entity, line)

	def process(line):
		return plantPlot_(entity, line)

	processPerLine(Rows, spawn, process)