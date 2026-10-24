from farmTypes_py import *

PetalLocations = {}

for count in range(MIN_SUNFLOWER_PETALS, MAX_SUNFLOWER_PETALS):
	PetalLocations[count] = []

# PLOT[SUNFLOWERS] = [(x, y)...] # Where all Sunflowers are Planted
for x, y in PLOT[SUNFLOWERS]:
	moveTo(x, y)
	plant(SUNFLOWER)

for x, y in PLOT[SUNFLOWERS]:
	moveTo(x, y)
	count = measure()
	PetalLocations[count].append((x,y))
	
# range(0, 3) -> 0, 1, 2 -> [0, 3)
# range(get_world_size()) -> 0, ..., 31
#PetalLocations = {
#	15 : [(x, y)...],
#	14 : [],
#	13 : [(x, y)...],
#	...
#}

for count in range(MAX_SUNFLOWER_PETALS, MIN_SUNFLOWER_PETALS, -1):
	for x, y in PetalLocations[count]:
		moveTo(x, y)
		harvest()
	