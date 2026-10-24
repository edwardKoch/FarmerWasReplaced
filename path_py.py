
#p1, p2: (x,y) coordinates
def manhattanDistance(p1, p2):
	# Unpack x, y and sum the horx/vert axis movements
	return abs(p1[0] - p2[0]) + abs(p1[1]+p2[1])
			
# Route: list of (x, y) coordinates to visit
def calculateRouteLength(route):
	totalDistance = 0
	
	for i in range(len(route) - 1):
		totalDistance += manhattanDistance(route[i], route[i+1])
		
	return totalDistance
	
# Returns optimized route
# Route: list of (x, y) coordinates to visit
def getShortestRoute(route):
	return greedyShortestRoute(route)

	
def greedyShortestRoute(route):
	if len(route) < 2:
		return route
		
	# make a copy of the route
	unvisited = list(route)
	
	start = unvisited.pop(0)
	optimizedRoute = [start]
	
	# As long as we have places to go
	while len(unvisited) > 0:
		current = optimizedRoute[-1]
		
		nearestNeighbor = unvisited[0]
		nearestDistance = manhattanDistance(current, nearestNeighbor)
	
		for neighbor in unvisited:
			dist = manhattanDistance(current, neighbor)
			if  dist < nearestDistance:
				nearestDistance = dist
				nearestNeighbor = neighbor
				
		optimizedRoute.append(nearestNeighbor)
		unvisited.remove(nearestNeighbor)
			
	return optimizedRoute