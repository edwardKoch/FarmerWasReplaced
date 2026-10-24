from motion_py import *

def bubbleSort(lst, fcn):
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
			  
# Define a coordinate compare for either x or y
# Idx: Index of coordinate to sort by (0, 1)
# Greater: True if check for greater than, false if less than
def dirCompare(idx, greater):
	if greater:
		def coordinateCompare(p1, p2):
			return p1[idx] > p2[idx]
	else:
		def coordinateCompare(p1, p2):
				return p1[idx] < p2[idx]

	return coordinateCompare


# Perform a Funciton per line, spawning as able
# Lines: Dict of x/y value to list of coords
# SpawnFcn: spawn_drone with correct arguments, takes in a single line
# ProcessFcn: some fcn() with the correct arguments, takes in a single line
# returns dict of x/y value to result of processFcn
def processPerLine(Lines, spawnFcn, processFcn):
	# Track workers as a (ID, xy) pair
	workers = []

	# Track results
	results = {}

	# Find the longest line, so that the
	# main worker always sorts that one
	# To avoid dead time while minions work
	maxLen = 0
	maxLenLine = -1
	for xy in Lines:
		length = len(Lines[xy])
		if length >= maxLen:
			maxLen = length
			maxLenLine = xy

	# For Each line in Lines[xy]
	for xy in Lines:
		line = Lines[xy]

		# Process the longest line last
		if xy == maxLenLine:
			continue
		else:
			# Attempt to spawna  worker for the line
			moveTo(line[0])
			worker = spawnFcn(line)
			if worker != None:
				workers.append((worker, xy))
			# If no workers available, process with main drone
			else:
				results[xy] = processFcn(line)

	# Process the longest line last
	if maxLenLine != -1:
		results[maxLenLine] = processFcn(Lines[maxLenLine])

	# Wait for all workers to be done - aggregate results
	for minion, xy in workers:
		results[xy] = wait_for(minion)

	return results