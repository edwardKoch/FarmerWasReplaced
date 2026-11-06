from _move_ import *

def bubbleSort(lst, fcn):
	# Bubble sort a list given a comparator funciton
	# lst: some list
	# fcn: comparator funciton, where if true, will swap
	n = len(lst)

	for i in range(n):
		swapped = False
		for j in range (0, n - i - 1):
			if fcn(lst[j], lst[j+1]):
				lst[j], lst[j+1] = lst[j+1], lst[j]
				swapped = True
		if not swapped:
			break

	return lst

def plotToRowsCols(plot):
	# Organizes a plot into a dict of rows and cols
	# plot: List of Tuples for coordinates (x, y)
	# RETURNS: Rows, Cols - dicts of {x|y : [(x,y)...]}
	
	# Split plot into Rows & cols
	Rows = {}
	Cols = {}

	dim = get_world_size()
	for i in range(dim):
		Rows[i] = []
		Cols[i] = []

	for square in plot:
		Rows[square[1]].append(square)
		Cols[square[0]].append(square)

	# Define bubble sort funciton
	def coordinateRowCompare(p1, p2):
		return p1[0] > p2[0]
	def coordinateColCompare(p1, p2):
		return p1[1] > p2[1]

	# Remove empty lists
	for i in range(dim):
		if len(Rows[i]) < 1:
			Rows.pop(i)
		if len(Cols[i]) < 1:
			Cols.pop(i)

	# Sort all Rows & Cols
	for row in Rows:
		bubbleSort(Rows[row], coordinateRowCompare)
	for col in Cols:
		bubbleSort(Cols[col], coordinateColCompare)

	return Rows, Cols
		


def processPerLine(Lines, spawnFcn, processFcn):
	# Perform a Funciton per line, spawning as able
	# Lines: Dict of x|y value to list of coords
	# spawnFcn: spawn_drone with correct arguments, takes in a single line
	# processFcn: some fcn() with the correct arguments, takes in a single line
	# RETURNS: dict of x|y value to result of processFcn
	
	# Track workers as a (ID, xy) pair
	workers = []

	# Track results
	results = {}

	# Track Key values to process
	keys = []
	for xy in Lines:
		keys.append(xy)

	# Save the last key for the 'main' drone
	last = keys[len(keys) - 1]

	# For Each line in Lines[xy]
	for xy in keys:
		if xy == last:
			break
		
		line = Lines[xy]

		# Attempt to spawna  worker for the line
		moveTo(line[0])
		worker = spawnFcn(line)
		if worker != None:
			workers.append((worker, xy))
		# If no workers available, process with main drone
		else:
			results[xy] = processFcn(line)

	# Process the last line
	results[last] = processFcn(Lines[last])

	# Wait for all workers to be done - aggregate results
	for minion, xy in workers:
		results[xy] = wait_for(minion)

	return results