from algorithms_py import *
from motion_py import *
from farming_py import *
from harvest_py import *
from plant_py import *

# Sort a 1D line of Cacti
# Line: List of squares in row/col
# Idx: Index of coordinate to sort by (0, 1)
def sortCacti(line):
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


# Sort a Dict of Rows or Cols
# Lines: Dict of x/y -> list of (x, y)
def cactusSort(lines):
	def spawn(line):
		return spawn_drone(sortCacti, line)

	def process(line):
		return sortCacti(line)

	processPerLine(lines, spawn, process)


def cactusWorker(conditionFcn):
	_dim = get_world_size()

	# Store all the rows
	Rows = ROWS[CACTUS]

	# Store all the cols
	Cols = COLS[CACTUS]

	# Process all Cacti
	while conditionFcn():

		# Initial Plant of All Cacti
		# No Fertilizer, No Water,  No Waiting, Force Harvest
		harvestAndPlantAllEntity(CACTUS, False, False, False, True)

		# Sort all Rows & Cols
		cactusSort(Rows)
		cactusSort(Cols)

		# Sort 2 times just in case the shape
		# of the plot corners something
		#cactusSort(Rows)
		#cactusSort(Cols)

		# Harvest all Catci
		# Should be a single harvest due to sorting
		harvest()
