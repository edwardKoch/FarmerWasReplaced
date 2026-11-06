from _move_ import *
from _algo_ import *
from _plant_ import *

def sortCacti(line):
	# Sort a 1D line of Cacti
	# Line: List of squares in row/col
	n = len(line)

	# if there are is 0 or 1 catci, they are sorted
	if n < 2:
		return

	# Use Shaker sort to optimize Drone travel time
	# Since Bubble sort requires travelling back to begining
	swapped = True
	start = 0
	end = n - 1

	while swapped:
		# Reset the swapped flag for each pass
		swapped = False

		# Forward Pass = Bubble Sort
		for i in range(start, end):
			# Get which direction to search in
			dir = getDir(line[i], line[i+1])
			moveTo(line[i])
			local = measure()
			neighbor = measure(dir)
			# Always sort biggest to the North or East
			if dir == North or dir == East:
				if local > neighbor:
					swap(dir)
					swapped = True
			else:
				if local < neighbor:
					swap(dir)
					swapped = True

		# if nothing moved, then cacti are sorted
		if not swapped:
			break

		# If something was moved, then we know the last 
		# entry is in the right place (bubble sort)
		end -= 1

		# Backwards Pass = Reverse bubble sort
		for i in range(end, start, -1):
			# Get which direction to search in
			dir = getDir(line[i], line[i-1])
			moveTo(line[i])
			local = measure()
			neighbor = measure(dir)
			# Always sort biggest to the North or East
			if dir == North or dir == East:
				if local > neighbor:
					swap(dir)
					swapped = True
			else:
				if local < neighbor:
					swap(dir)
					swapped = True

		# If nothing was moved, while loop will exit

		# If something was moved, then we know the first 
		# entry is in the right place (reverse bubble sort)
		start += 1

def sortCactusPlot(plot):
	# Sort a plot of cacti
	# plot: List of Tuples for coordinates (x, y)
	
	# Split plot into Rows & cols
	Rows, Cols = plotToRowsCols(plot)

	# Sort all Rows & Cols
	for row in Rows:
		sortCacti(Rows[row])
	for col in Cols:
		sortCacti(Cols[col])

	# Sort 2 times just in case the shape
	# of the plot corners something
	#for row in Rows:
	#	sortCacti(Rows[row])
	#for col in Cols:
	#    sortCacti(Cols[col])
	

def processCactiPlot(plot):
	# Process Cacti Plot until harvested
	# plot: List of Tuples for coordinates (x, y)

	# Plant first round of Cacti
	for x, y in plot:
		moveTo((x,y))
		if get_entity_type() != Entities.Cactus:
			plant(Entities.Cactus)

	# Sort all of the cacti to the NE
	sortCactusPlot(plot)

	# Sorted Cacti are harvested all at once
	harvest()

def processCactiPlotMulti(plot):
	# Process Cacti Plot until harvested - using multiple drones
	
	# Plant first round of Cacti
	plantPlotMulti_(Entities.Cactus, plot)

	# Split plot into Rows & cols
	Rows, Cols = plotToRowsCols(plot)
			
	def spawn(line):
		return spawn_drone(sortCacti, line)

	def process(line):
		return sortCacti(line)

	processPerLine(Rows, spawn, process)
	processPerLine(Cols, spawn, process)

	harvest()