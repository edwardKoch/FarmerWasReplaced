from _move_ import *

def processPolyPlot(plot):
	# Perform one PolutCulture Plant Cycle
	# plot: list of (x,y) coordinates to plant
	
	# Track what squares we have been to
	visited = {}
	for sq in plot:
		visited[sq] = False

	# Start in the middle of the plot
	entity = Entities.Grass
	space = plot[(len(plot)//2)]

	complete = False
	while not complete:
		moveTo(space)
		visited[space] = True
		harvest()
		plant(entity)
		
		newEntity, newSpace = get_companion()
		
		# Plant current entity
		# until the companion is within the plot
		# only try a certain number of times
		count = len(plot) // 2
		while count >= 0:
			count -= 1
			harvest()
			plant(entity)
			newEntity, newSpace = get_companion()

			if (newSpace in plot and not visited[newSpace]):
				break

		# If unable to find a sutible spot, just harvest and be done
		if count < 0:
			break

		else:

			entity, space = newEntity, newSpace

			# Check to see if all spaces have been visited
			complete = True
			for v in visited:
				if not visited[v]:
					complete = False
					break

	# Harvest the whole plot
	for sq in plot:
		moveTo(sq)
		harvest()
			