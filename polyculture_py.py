from motion_py import *
from farming_py import *
from harvest_py import *
from plant_py import *

# Repeatedly do polyculture farming
def polyWorker(conditionFcn, centerX, centerY, plotWidth):
	cX, cY = centerX, centerY
	center = (cX, cY)

	# PolyCulture Test
	plot = []

	left = -(plotWidth //2)
	right = (plotWidth //2) + 1

	for x in range(left, right):
		for y in range(left, right):
			plot.append((cX + x, cY + y))

	moveTo(center)

	while conditionFcn():
		visited = {}
		for sq in plot:
			visited[sq] = False
			
		v = 0
		entity = GRASS
		space = None

		moveTo(center)
		harvestAndPlant(entity, False, True, False, True)

		complete = False
		# Fill the whole plot
		while not complete:

			# Generate a new companion square
			# In the plot that we havent visited before
			# Limit searches for sanity
			maxSearch = 25
			count = 0
			while count < maxSearch:
				count += 1
				newEntity, newSpace = get_companion()
				# If a unique companion is found, break
				if (newSpace in plot and visited[newSpace] != True):
					entity, space = newEntity, newSpace
					break
				# If a new companion isnt found
				# Replant and try again, force the harvest
				harvestAndPlant(entity, False, False, False, True)

			# If we gave up, just harvest the plot and start over
			if count >= maxSearch:
				break

			# Go to the companion square
			moveTo(space)
			visited[space] = True
			# Plant the companion, no fert, water, no block, no force
			harvestAndPlant(entity, False, True, False, False)

			# check if we have visited every square
			complete = True
			for s in visited:
				if not visited[s]:
					complete = False
					break

		# Harvest the whole plot
		for space in plot:
			moveTo(space)
			harvestEntity(True, False)